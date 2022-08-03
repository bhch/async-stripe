from stripe import util
from stripe import api_requestor
from stripe.stripe_object import StripeObject
from stripe.api_resources.abstract.api_resource import APIResource


async def _static_request_patch(
    cls,
    method_,
    url_,
    api_key=None,
    idempotency_key=None,
    stripe_version=None,
    stripe_account=None,
    params=None
):
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    headers = util.populate_headers(idempotency_key)
    response, api_key = await requestor.request(method_, url_, params, headers)
    return util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account, params
    )

APIResource._static_request = classmethod(_static_request_patch)


async def _static_request_stream_patch(
    cls,
    method_,
    url_,
    api_key=None,
    idempotency_key=None,
    stripe_version=None,
    stripe_account=None,
    params=None
):
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    headers = util.populate_headers(idempotency_key)
    response, _ = await requestor.request_stream(method_, url_, params, headers)
    return response

APIResource._static_request_stream = classmethod(_static_request_stream_patch)


async def retrieve_patch(cls, id, api_key=None, **params):
    instance = cls(id, api_key, **params)
    await instance.refresh()
    return instance

APIResource.retrieve = classmethod(retrieve_patch)


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
    obj = await StripeObject._request(
        self,
        method_,
        url_,
        api_key,
        idempotency_key,
        stripe_version,
        stripe_account,
        headers,
        params,
    )

    if type(self) is type(obj):
        self.refresh_from(obj)
        return self
    else:
        return obj

APIResource._request = _request_patch


async def _request_and_refresh_patch(
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
    obj = await StripeObject._request(
        self,
        method_,
        url_,
        api_key,
        idempotency_key,
        stripe_version,
        stripe_account,
        headers,
        params,
    )

    self.refresh_from(obj)
    return self

APIResource._request_and_refresh = _request_and_refresh_patch
