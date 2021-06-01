from stripe import util
from stripe.api_resources.abstract.listable_api_resource import (
    ListableAPIResource,
)
from async_stripe.api_requestor import AsyncAPIRequestor


async def list_patch(
    cls, api_key=None, stripe_version=None, stripe_account=None, **params
):
    requestor = AsyncAPIRequestor(
        api_key,
        api_base=cls.api_base(),
        api_version=stripe_version,
        account=stripe_account,
    )
    url = cls.class_url()
    response, api_key = await requestor.request("get", url, params)
    stripe_object = util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )
    stripe_object._retrieve_params = params
    return stripe_object


for subclass in ListableAPIResource.__subclasses__():
    subclass.list = classmethod(list_patch)
