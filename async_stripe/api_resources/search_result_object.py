import stripe
from stripe import api_requestor, six, util
from stripe.stripe_object import StripeObject

from stripe.six.moves.urllib.parse import quote_plus


async def search_patch(
    self, api_key=None, stripe_version=None, stripe_account=None, **params
):
    stripe_object = await self._request(
        "get",
        self.get("url"),
        api_key=api_key,
        stripe_version=stripe_version,
        stripe_account=stripe_account,
        **params
    )
    stripe_object._retrieve_params = params
    return stripe_object


async def _request_patch(
    self,
    method_,
    url_,
    api_key=None,
    idempotency_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    api_key = api_key or self.api_key
    stripe_version = stripe_version or self.stripe_version
    stripe_account = stripe_account or self.stripe_account

    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    headers = util.populate_headers(idempotency_key)
    response, api_key = await requestor.request(method_, url_, params, headers)
    stripe_object = util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )
    return stripe_object


async def auto_paging_iter_patch(self):
    page = self

    while True:
        for item in page:
            yield item
        page = await page.next_search_result_page()

        if page.is_empty:
            break


async def next_search_result_page_patch(
    self, api_key=None, stripe_version=None, stripe_account=None, **params
):
    if not self.has_more:
        return self.empty_search_result(
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
        )

    params_with_filters = self._retrieve_params.copy()
    params_with_filters.update({"page": self.next_page})
    params_with_filters.update(params)

    return await self.search(
        api_key=api_key,
        stripe_version=stripe_version,
        stripe_account=stripe_account,
        **params_with_filters
    )


stripe.SearchResultObject.search = search_patch
stripe.SearchResultObject._request = _request_patch
stripe.SearchResultObject.auto_paging_iter = auto_paging_iter_patch
stripe.SearchResultObject.next_search_result_page = next_search_result_page_patch
