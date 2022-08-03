import stripe


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


stripe.SearchResultObject.auto_paging_iter = auto_paging_iter_patch
stripe.SearchResultObject.next_search_result_page = next_search_result_page_patch
