from stripe import util

from stripe.api_resources.abstract.createable_api_resource import (
    CreateableAPIResource,
)
from async_stripe.api_requestor import AsyncAPIRequestor

async def create_patch(
    cls,
    api_key=None,
    idempotency_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    requestor = AsyncAPIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    url = cls.class_url()
    headers = util.populate_headers(idempotency_key)
    response, api_key = await requestor.request("post", url, params, headers)

    return util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )


for subclass in CreateableAPIResource.__subclasses__():
    subclass.create = classmethod(create_patch)