from stripe.api_resources.abstract.listable_api_resource import (
    ListableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from typing import Awaitable


async def auto_paging_iter_patch(cls, *args, **params):
    obj = await cls.list(*args, **params)
    return obj.auto_paging_iter()


def list_patch(
    cls, api_key=None, stripe_version=None, stripe_account=None, **params
) -> Awaitable[ListObject]:
    result = cls._static_request(
        "get",
        cls.class_url(),
        api_key=api_key,
        stripe_version=stripe_version,
        stripe_account=stripe_account,
        params=params,
    )

    if not isinstance(result, Awaitable):
        raise TypeError(
            "Expected awaitable object from API, got %s"
            % (type(result).__name__,)
        )

    return result


ListableAPIResource.auto_paging_iter = classmethod(auto_paging_iter_patch)
ListableAPIResource.list = classmethod(list_patch)


for subclass in ListableAPIResource.__subclasses__():
    subclass.auto_paging_iter = classmethod(auto_paging_iter_patch)
