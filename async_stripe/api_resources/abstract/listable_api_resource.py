from stripe.api_resources.abstract.listable_api_resource import (
    ListableAPIResource,
)


async def auto_paging_iter_patch(cls, *args, **params):
    obj = await cls.list(*args, **params)
    return obj.auto_paging_iter()


ListableAPIResource.auto_paging_iter = classmethod(auto_paging_iter_patch)


for subclass in ListableAPIResource.__subclasses__():
    subclass.auto_paging_iter = classmethod(auto_paging_iter_patch)
