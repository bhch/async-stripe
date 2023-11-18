from __future__ import absolute_import, division, print_function

import pytest
import json
import asyncio

import stripe
import urllib3
from stripe import util

from async_stripe.http_client import TornadoAsyncHTTPClient


pytestmark = pytest.mark.asyncio

VALID_API_METHODS = ("get", "post", "delete")


class StripeClientTestCase(object):
    REQUEST_LIBRARIES = [
        ("AsyncHTTPClient", "async_stripe.http_client.AsyncHTTPClient"),
    ]

    @pytest.fixture
    def request_mocks(self, mocker):
        request_mocks = {}
        for lib, mockpath in self.REQUEST_LIBRARIES:
            request_mocks[lib] = mocker.patch(mockpath)
        return request_mocks


class TestNewDefaultHttpClient(StripeClientTestCase):
    @pytest.fixture(autouse=True)
    def setup_warnings(self, request_mocks):
        original_filters = stripe.http_client.warnings.filters[:]
        stripe.http_client.warnings.simplefilter("ignore")
        yield
        stripe.http_client.warnings.filters = original_filters

    def check_default(self, none_libs, expected):
        for lib in none_libs:
            setattr(stripe.http_client, lib, None)

        inst = stripe.http_client.new_default_http_client()

        assert isinstance(inst, expected)

    def test_new_default_http_client_tornado(self):
        self.check_default((), TornadoAsyncHTTPClient)

    


class TestRetrySleepTimeDefaultHttpClient(StripeClientTestCase):
    from contextlib import contextmanager

    def assert_sleep_times(self, client, expected):
        until = len(expected)
        actual = list(
            map(lambda i: client._sleep_time_seconds(i + 1), range(until))
        )
        assert expected == actual

    @contextmanager
    def mock_max_delay(self, new_value):
        original_value = stripe.http_client.HTTPClient.MAX_DELAY
        stripe.http_client.HTTPClient.MAX_DELAY = new_value
        try:
            yield self
        finally:
            stripe.http_client.HTTPClient.MAX_DELAY = original_value

    def test_sleep_time_exponential_back_off(self):
        client = stripe.http_client.new_default_http_client()
        client._add_jitter_time = lambda t: t
        with self.mock_max_delay(10):
            self.assert_sleep_times(client, [0.5, 1.0, 2.0, 4.0, 8.0])

    def test_initial_delay_as_minimum(self):
        client = stripe.http_client.new_default_http_client()
        client._add_jitter_time = lambda t: t * 0.001
        initial_delay = stripe.http_client.HTTPClient.INITIAL_DELAY
        self.assert_sleep_times(client, [initial_delay] * 5)

    def test_maximum_delay(self):
        client = stripe.http_client.new_default_http_client()
        client._add_jitter_time = lambda t: t
        max_delay = stripe.http_client.HTTPClient.MAX_DELAY
        expected = [0.5, 1.0, max_delay, max_delay, max_delay]
        self.assert_sleep_times(client, expected)

    def test_retry_after_header(self):
        client = stripe.http_client.new_default_http_client()
        client._add_jitter_time = lambda t: t

        # Prefer retry-after if it's bigger
        assert 30 == client._sleep_time_seconds(
            2, (None, 409, {"retry-after": "30"})
        )
        # Prefer default if it's bigger
        assert 2 == client._sleep_time_seconds(
            3, (None, 409, {"retry-after": "1"})
        )
        # Ignore crazy-big values
        assert 1 == client._sleep_time_seconds(
            2, (None, 409, {"retry-after": "300"})
        )

    def test_randomness_added(self):
        client = stripe.http_client.new_default_http_client()
        random_value = 0.8
        client._add_jitter_time = lambda t: t * random_value
        base_value = stripe.http_client.HTTPClient.INITIAL_DELAY * random_value

        with self.mock_max_delay(10):
            expected = [
                stripe.http_client.HTTPClient.INITIAL_DELAY,
                base_value * 2,
                base_value * 4,
                base_value * 8,
                base_value * 16,
            ]
            self.assert_sleep_times(client, expected)

    def test_jitter_has_randomness_but_within_range(self):
        client = stripe.http_client.new_default_http_client()

        jittered_ones = set(
            map(lambda _: client._add_jitter_time(1), list(range(100)))
        )

        assert len(jittered_ones) > 1
        assert all(0.5 <= val <= 1 for val in jittered_ones)


class TestRetryConditionsDefaultHttpClient(StripeClientTestCase):
    def test_should_retry_on_codes(self):
        one_xx = list(range(100, 104))
        two_xx = list(range(200, 209))
        three_xx = list(range(300, 308))
        four_xx = list(range(400, 431))

        client = stripe.http_client.new_default_http_client()
        client._max_network_retries = lambda: 1
        codes = one_xx + two_xx + three_xx + four_xx
        codes.remove(409)

        # These status codes should not be retried by default.
        for code in codes:
            assert client._should_retry((None, code, None), None, 0) is False

        # These status codes should be retried by default.
        assert client._should_retry((None, 409, None), None, 0) is True
        assert client._should_retry((None, 500, None), None, 0) is True
        assert client._should_retry((None, 503, None), None, 0) is True

    def test_should_retry_on_error(self, mocker):
        client = stripe.http_client.new_default_http_client()
        client._max_network_retries = lambda: 1
        api_connection_error = mocker.Mock()

        api_connection_error.should_retry = True
        assert client._should_retry(None, api_connection_error, 0) is True

        api_connection_error.should_retry = False
        assert client._should_retry(None, api_connection_error, 0) is False

    def test_should_retry_on_stripe_should_retry_true(self, mocker):
        client = stripe.http_client.new_default_http_client()
        client._max_network_retries = lambda: 1
        headers = {"stripe-should-retry": "true"}

        # Ordinarily, we would not retry a 400, but with the header as true, we would.
        assert client._should_retry((None, 400, {}), None, 0) is False
        assert client._should_retry((None, 400, headers), None, 0) is True

    def test_should_retry_on_stripe_should_retry_false(self, mocker):
        client = stripe.http_client.new_default_http_client()
        client._max_network_retries = lambda: 1
        headers = {"stripe-should-retry": "false"}

        # Ordinarily, we would retry a 500, but with the header as false, we would not.
        assert client._should_retry((None, 500, {}), None, 0) is True
        assert client._should_retry((None, 500, headers), None, 0) is False

    def test_should_retry_on_num_retries(self, mocker):
        client = stripe.http_client.new_default_http_client()
        max_test_retries = 10
        client._max_network_retries = lambda: max_test_retries
        api_connection_error = mocker.Mock()
        api_connection_error.should_retry = True

        assert (
            client._should_retry(
                None, api_connection_error, max_test_retries + 1
            )
            is False
        )
        assert (
            client._should_retry((None, 409, None), None, max_test_retries + 1)
            is False
        )


class TestHTTPClient(object):
    @pytest.fixture(autouse=True)
    def setup_stripe(self):
        orig_attrs = {"enable_telemetry": stripe.enable_telemetry}
        stripe.enable_telemetry = False
        yield
        stripe.enable_telemetry = orig_attrs["enable_telemetry"]

    async def test_sends_telemetry_on_second_request(self, mocker):
        class TestClient(stripe.http_client.HTTPClient):
            pass

        stripe.enable_telemetry = True

        url = "http://fake.url"

        client = TestClient()

        response_future = asyncio.Future()
        response_future.set_result(["", 200, {"Request-Id": "req_123"}])

        client.request = mocker.MagicMock(
            return_value=response_future
        )

        _, code, _ = await client.request_with_retries("get", url, {}, None)
        assert code == 200
        client.request.assert_called_with("get", url, {}, None)

        response_future = asyncio.Future()
        response_future.set_result(["", 200, {"Request-Id": "req_234"}])

        client.request = mocker.MagicMock(
            return_value=response_future
        )
        _, code, _ = await client.request_with_retries("get", url, {}, None)
        assert code == 200
        args, _ = client.request.call_args
        assert "X-Stripe-Client-Telemetry" in args[2]

        telemetry = json.loads(args[2]["X-Stripe-Client-Telemetry"])
        assert telemetry["last_request_metrics"]["request_id"] == "req_123"


class ClientTestBase(object):
    @pytest.fixture
    def request_mock(self, request_mocks):
        return request_mocks[self.REQUEST_CLIENT.name]

    @property
    def valid_url(self, path="/foo"):
        return "https://api.stripe.com%s" % (path,)

    def make_request(self, method, url, headers, post_data):
        client = self.REQUEST_CLIENT(verify_ssl_certs=True)
        return client.request_with_retries(method, url, headers, post_data)

    async def make_request_stream(self, method, url, headers, post_data):
        client = self.REQUEST_CLIENT(verify_ssl_certs=True)
        return await client.request_stream_with_retries(
            method, url, headers, post_data
        )

    @pytest.fixture
    def mock_response(self):
        def mock_response(mock, body, code):
            raise NotImplementedError(
                "You must implement this in your test subclass"
            )

        return mock_response

    @pytest.fixture
    def mock_error(self):
        def mock_error(mock, error):
            raise NotImplementedError(
                "You must implement this in your test subclass"
            )

        return mock_error

    @pytest.fixture
    def check_call(self):
        def check_call(
            mock, method, abs_url, headers, params, is_streaming=False
        ):
            raise NotImplementedError(
                "You must implement this in your test subclass"
            )

        return check_call

    def test_request(self, request_mock, mock_response, check_call):
        mock_response(request_mock, '{"foo": "baz"}', 200)

        for method in VALID_API_METHODS:
            abs_url = self.valid_url
            data = ""

            if method != "post":
                abs_url = "%s?%s" % (abs_url, data)
                data = None

            headers = {"my-header": "header val"}

            body, code, _ = self.make_request(method, abs_url, headers, data)

            assert code == 200
            assert body == '{"foo": "baz"}'

            check_call(request_mock, method, abs_url, data, headers)

    def test_request_stream(
        self, mocker, request_mock, mock_response, check_call
    ):
        for method in VALID_API_METHODS:
            mock_response(request_mock, "some streamed content", 200)

            abs_url = self.valid_url
            data = ""

            if method != "post":
                abs_url = "%s?%s" % (abs_url, data)
                data = None

            headers = {"my-header": "header val"}

            print(dir(self))
            print("make_request_stream" in dir(self))
            stream, code, _ = self.make_request_stream(
                method, abs_url, headers, data
            )

            assert code == 200

            # Here we need to convert and align all content on one type (string)
            # as some clients return a string stream others a byte stream.
            body_content = stream.read()
            if hasattr(body_content, "decode"):
                body_content = body_content.decode("utf-8")

            assert body_content == "some streamed content"

            mocker.resetall()

    def test_exception(self, request_mock, mock_error):
        mock_error(request_mock)
        with pytest.raises(stripe.error.APIConnectionError):
            self.make_request("get", self.valid_url, {}, None)


class TestTornadoAsyncHTTPClient:
    # :TODO: Write tests for tornado client
    pass


class TestAPIEncode(StripeClientTestCase):
    def test_encode_dict(self):
        body = {"foo": {"dob": {"month": 1}, "name": "bat"}}

        values = [t for t in stripe.api_requestor._api_encode(body)]

        assert ("foo[dob][month]", 1) in values
        assert ("foo[name]", "bat") in values

    def test_encode_array(self):
        body = {"foo": [{"dob": {"month": 1}, "name": "bat"}]}

        values = [t for t in stripe.api_requestor._api_encode(body)]

        assert ("foo[0][dob][month]", 1) in values
        assert ("foo[0][name]", "bat") in values
