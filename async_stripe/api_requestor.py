from stripe import error, version, util, six
from stripe.multipart_data_generator import MultipartDataGenerator
from stripe.six.moves.urllib.parse import urlencode

from stripe.api_requestor import APIRequestor
from stripe.api_requestor import _build_api_url, _api_encode

from tornado.httpclient import AsyncHTTPClient, HTTPError


client = AsyncHTTPClient()


async def request_patch(self, method, url, params=None, headers=None):
    rbody, rcode, rheaders, my_api_key = await self.request_raw(
        method.lower(), url, params, headers
    )
    resp = self.interpret_response(rbody, rcode, rheaders)
    return resp, my_api_key


APIRequestor.request = request_patch 


async def request_raw_patch(self, method, url, params=None, supplied_headers=None):
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

    # :TODO: Add telemetry headers as done by the official library
    # :TODO: Add retry support on error
    try:
        response = await client.fetch(
            abs_url, 
            method=method.upper(), 
            headers=headers, 
            body=post_data
        )
    except HTTPError as e:
        if e.response:
            rbody = e.response.body
            rcode = e.response.code
            rheaders = dict(e.response.headers)
        else:
            rbody = ''
            rcode = ''
            rheaders = {}
    except Exception as e:
        raise error.APIConnectionError("Network error: Couldn't connet to stripe")
    else:
        rbody = response.body
        rcode = response.code
        rheaders = dict(response.headers)

    util.log_info("Stripe API response", path=abs_url, response_code=rcode)
    util.log_debug("API response body", body=rbody)

    if "Request-Id" in rheaders:
        request_id = rheaders["Request-Id"]
        util.log_debug(
            "Dashboard link for request",
            link=util.dashboard_link(request_id),
        )

    return rbody, rcode, rheaders, my_api_key



APIRequestor.request_raw = request_raw_patch