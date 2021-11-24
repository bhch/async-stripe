from stripe import util
from stripe import api_requestor
from stripe.api_resources.abstract.api_resource import APIResource


async def _static_request_patch(
    cls,
    method_,
    url_,
    api_key=None,
    idempotency_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    headers = util.populate_headers(idempotency_key)
    response, api_key = await requestor.request(method_, url_, params, headers)
    return util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
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
    **params
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


async def refresh_patch(self):
    self.refresh_from(await self.request("get", self.instance_url()))
    return self

APIResource.refresh = refresh_patch
