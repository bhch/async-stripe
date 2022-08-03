from stripe import util
from stripe.stripe_object import StripeObject
from stripe import api_requestor


async def _request_patch(
    self,
    method_,
    url_,
    api_key=None,
    idempotency_key=None,
    stripe_version=None,
    stripe_account=None,
    headers=None,
    params=None,
):
    stripe_account = stripe_account or self.stripe_account
    stripe_version = stripe_version or self.stripe_version
    api_key = api_key or self.api_key
    params = params or self._retrieve_params

    requestor = api_requestor.APIRequestor(
        key=api_key,
        api_base=self.api_base(),
        api_version=stripe_version,
        account=stripe_account,
    )

    if idempotency_key is not None:
        headers = {} if headers is None else headers.copy()
        headers.update(util.populate_headers(idempotency_key))

    response, api_key = await requestor.request(method_, url_, params, headers)

    return util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account, params
    )

StripeObject._request = _request_patch


async def request_stream_patch(self, method, url, params=None, headers=None):
    if params is None:
        params = self._retrieve_params
    requestor = api_requestor.APIRequestor(
        key=self.api_key,
        api_base=self.api_base(),
        api_version=self.stripe_version,
        account=self.stripe_account,
    )
    response, _ = await requestor.request_stream(method, url, params, headers)

    return response

StripeObject.request_stream = request_stream_patch
