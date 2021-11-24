from stripe import util
from stripe.stripe_object import StripeObject
from stripe import api_requestor


async def request_patch(self, method, url, params=None, headers=None):
    if params is None:
        params = self._retrieve_params

    requestor = api_requestor.APIRequestor(
        key=self.api_key,
        api_base=self.api_base(),
        api_version=self.stripe_version,
        account=self.stripe_account,
    )

    response, api_key = await requestor.request(method, url, params, headers)

    return util.convert_to_stripe_object(
        response, api_key, self.stripe_version, self.stripe_account
    )

StripeObject.request = request_patch


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
