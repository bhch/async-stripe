import stripe
from stripe import error, version, util, six
from stripe.multipart_data_generator import MultipartDataGenerator
from stripe.six.moves.urllib.parse import urlencode

from stripe.api_requestor import APIRequestor
from stripe.api_requestor import _build_api_url, _api_encode

from async_stripe import http_client


def init_patch(
    self,
    key=None,
    client=None,
    api_base=None,
    api_version=None,
    account=None,
):
    self.api_base = api_base or stripe.api_base
    self.api_key = key
    self.api_version = api_version or stripe.api_version
    self.stripe_account = account

    self._default_proxy = None

    from stripe import verify_ssl_certs as verify
    from stripe import proxy

    # only use client if mockclient (for testing)
    # otherwise use Tornado client
    if client:
        if client.name == 'mockclient':
            self._client = client
    elif stripe.default_http_client and \
        (
            stripe.default_http_client.name == 'mockclient' or \
            isinstance(stripe.default_http_client, http_client.TornadoAsyncHTTPClient)
        ):

        self._client = stripe.default_http_client
        if proxy != self._default_proxy:
            warnings.warn(
                "stripe.proxy was updated after sending a "
                "request - this is a no-op. To use a different proxy, "
                "set stripe.default_http_client to a new client "
                "configured with the proxy."
            )
    else:
        # If the stripe.default_http_client has not been set by the user
        # yet, we'll set it here. This way, we aren't creating a new
        # HttpClient for every request.
        stripe.default_http_client = http_client.new_default_http_client(
            verify_ssl_certs=verify, proxy=proxy
        )
        self._client = stripe.default_http_client
        self._default_proxy = proxy


APIRequestor.__init__ = init_patch


async def request_patch(self, method, url, params=None, headers=None):
    rbody, rcode, rheaders, my_api_key = await self.request_raw(
        method.lower(), url, params, headers, is_streaming=False
    )
    resp = self.interpret_response(rbody, rcode, rheaders)
    return resp, my_api_key


APIRequestor.request = request_patch 


async def request_stream_patch(self, method, url, params=None, headers=None):
    stream, rcode, rheaders, my_api_key = await self.request_raw(
        method.lower(), url, params, headers, is_streaming=True
    )
    resp = self.interpret_streaming_response(stream, rcode, rheaders)
    return resp, my_api_key


APIRequestor.request_stream = request_stream_patch


async def request_raw_patch(self, method, url, params=None, supplied_headers=None, is_streaming=False):
    """
    Mechanism for issuing an API call
    """

    if self.api_key:
        my_api_key = self.api_key
    else:
        from stripe import api_key

        my_api_key = api_key

    if my_api_key is None:
        raise error.AuthenticationError(
            "No API key provided. (HINT: set your API key using "
            '"stripe.api_key = <API-KEY>"). You can generate API keys '
            "from the Stripe web interface.  See https://stripe.com/api "
            "for details, or email support@stripe.com if you have any "
            "questions."
        )

    abs_url = "%s%s" % (self.api_base, url)

    encoded_params = urlencode(list(_api_encode(params or {})))

    # Don't use strict form encoding by changing the square bracket control
    # characters back to their literals. This is fine by the server, and
    # makes these parameter strings easier to read.
    encoded_params = encoded_params.replace("%5B", "[").replace("%5D", "]")

    if method == "get" or method == "delete":
        if params:
            abs_url = _build_api_url(abs_url, encoded_params)
        post_data = None
    elif method == "post":
        if (
            supplied_headers is not None
            and supplied_headers.get("Content-Type")
            == "multipart/form-data"
        ):
            generator = MultipartDataGenerator()
            generator.add_params(params or {})
            post_data = generator.get_post_data()
            supplied_headers[
                "Content-Type"
            ] = "multipart/form-data; boundary=%s" % (generator.boundary,)
        else:
            post_data = encoded_params
    else:
        raise error.APIConnectionError(
            "Unrecognized HTTP method %r.  This may indicate a bug in the "
            "Stripe bindings.  Please contact support@stripe.com for "
            "assistance." % (method,)
        )

    headers = self.request_headers(my_api_key, method)
    if supplied_headers is not None:
        for key, value in six.iteritems(supplied_headers):
            headers[key] = value

    util.log_info("Request to Stripe api", method=method, path=abs_url)
    util.log_debug(
        "Post details",
        post_data=encoded_params,
        api_version=self.api_version,
    )

    if is_streaming:
        (
            rcontent,
            rcode,
            rheaders,
        ) = await self._client.request_stream_with_retries(
            method, abs_url, headers, post_data
        )
    else:
        rcontent, rcode, rheaders = await self._client.request_with_retries(
            method, abs_url, headers, post_data
        )
    
    util.log_info("Stripe API response", path=abs_url, response_code=rcode)
    util.log_debug("API response body", body=rcontent)

    if "Request-Id" in rheaders:
        request_id = rheaders["Request-Id"]
        util.log_debug(
            "Dashboard link for request",
            link=util.dashboard_link(request_id),
        )

    return rcontent, rcode, rheaders, my_api_key


APIRequestor.request_raw = request_raw_patch
