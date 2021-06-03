from stripe import util
from stripe import api_requestor
from stripe.api_resources.abstract.listable_api_resource import (
    ListableAPIResource,
)


async def auto_paging_iter_patch(cls, *args, **params):
    obj = await cls.list(*args, **params)
    return obj.auto_paging_iter()


async def list_patch(
    cls, api_key=None, stripe_version=None, stripe_account=None, **params
):
    requestor = api_requestor.APIRequestor(
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


ListableAPIResource.auto_paging_iter = classmethod(auto_paging_iter_patch)
ListableAPIResource.list = classmethod(list_patch)


for subclass in ListableAPIResource.__subclasses__():
    subclass.auto_paging_iter = classmethod(auto_paging_iter_patch)
    subclass.list = classmethod(list_patch)
