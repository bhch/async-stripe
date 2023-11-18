from stripe.api_resources.abstract.searchable_api_resource import (
    SearchableAPIResource,
)
from stripe.api_resources.search_result_object import SearchResultObject
from typing import Awaitable


def _search_patch(
    cls,
    search_url,
    api_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
) -> Awaitable[SearchResultObject]:
    ret = cls._static_request(
        "get",
        search_url,
        api_key=api_key,
        stripe_version=stripe_version,
        stripe_account=stripe_account,
        params=params,
    )
    if not isinstance(ret, Awaitable):
        raise TypeError(
            "Expected awaitable object from API, got %s"
            % (type(ret).__name__,)
        )

    return ret


SearchableAPIResource._search = classmethod(_search_patch)