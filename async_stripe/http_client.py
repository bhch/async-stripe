import textwrap

import stripe
from stripe import error, util
from stripe.http_client import HTTPClient, _now_ms

from tornado import gen
from tornado.httpclient import AsyncHTTPClient, HTTPError


def new_default_http_client(*args, **kwargs):
    impl = TornadoAsyncHTTPClient

    return impl(*args, **kwargs)


stripe.http_client.new_default_http_client = new_default_http_client


class TornadoAsyncHTTPClient(HTTPClient):
    name = "tornado_async_http_client"

    def __init__(self, request_timeout=80, **kwargs):
        super().__init__(**kwargs)
        self.request_timeout = request_timeout
        self.client = AsyncHTTPClient()

    async def request_with_retries(self, method, url, headers, post_data=None):
        return await self._request_with_retries_internal(
            method, url, headers, post_data, is_streaming=False
        )

    async def request_stream_with_retries(self, method, url, headers, post_data=None):
        return await self._request_with_retries_internal(
            method, url, headers, post_data, is_streaming=True
        )

    async def _request_with_retries_internal(self, method, url, headers, post_data, is_streaming):
        self._add_telemetry_header(headers)

        num_retries = 0

        while True:
            request_start = _now_ms()

            try:
                if is_streaming:
                    response = await self.request_stream(
                        method, url, headers, post_data
                    )
                else:
                    response = await self.request(method, url, headers, post_data)
                connection_error = None
            except error.APIConnectionError as e:
                connection_error = e
                response = None

            if self._should_retry(response, connection_error, num_retries):
                if connection_error:
                    util.log_info(
                        "Encountered a retryable error %s"
                        % connection_error.user_message
                    )
                num_retries += 1
                sleep_time = self._sleep_time_seconds(num_retries, response)
                util.log_info(
                    (
                        "Initiating retry %i for request %s %s after "
                        "sleeping %.2f seconds."
                        % (num_retries, method, url, sleep_time)
                    )
                )
                await gen.sleep(sleep_time)
            else:
                if response is not None:
                    self._record_request_metrics(response, request_start)

                    return response
                else:
                    raise connection_error

    async def request(self, method, url, headers, post_data=None):
        return await self._request_internal(
            method, url, headers, post_data, is_streaming=False
        )

    async def request_stream(self, method, url, headers, post_data=None):
        return await self._request_internal(
            method, url, headers, post_data, is_streaming=True
        )

    async def _request_internal(self, method, url, headers, post_data, is_streaming):
        try:
            response = await self.client.fetch(
                url, 
                method=method.upper(), 
                headers=headers, 
                body=post_data,
                request_timeout=self.request_timeout
            )
        except HTTPError as e:
            if e.response:
                content = e.response.body
                status_code = e.response.code
                headers = dict(e.response.headers)
            else:
                self._handle_request_error(e)
        except Exception as e:
            self._handle_request_error(e)
        else:
            if is_streaming:
                # :TODO:
                # Currently, the full response is downloaded at once
                # It will be better to actually stream response in chunks
                content = util.io.BytesIO(response.body)
            else:
                content = response.body
            status_code = response.code
            headers = dict(response.headers)
        return content, status_code, headers

    def _handle_request_error(self, e):
        msg = (
            "Unexpected error communicating with Stripe. "
            "If this problem persists, let us know at support@stripe.com."
        )
        msg = textwrap.fill(msg) + "\n\n(Network error: " + str(e) + ")"
        raise error.APIConnectionError(msg)

    def close(self):
        pass


# also patch base class
HTTPClient.request_with_retries = TornadoAsyncHTTPClient.request_with_retries
HTTPClient.request_stream_with_retries = TornadoAsyncHTTPClient.request_stream_with_retries
HTTPClient._request_with_retries_internal = TornadoAsyncHTTPClient._request_with_retries_internal