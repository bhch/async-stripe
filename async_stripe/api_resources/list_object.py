# -*- coding: utf-8 -*-
import stripe


async def auto_paging_iter_patch(self):
    page = self

    while True:
        if (
            "ending_before" in self._retrieve_params
            and "starting_after" not in self._retrieve_params
        ):
            for item in reversed(page):
                yield item
            page = await page.previous_page()
        else:
            for item in page:
                yield item
            page = await page.next_page()

        if page.is_empty:
            break

async def next_page_patch(
    self, api_key=None, stripe_version=None, stripe_account=None, **params
):
    if not self.has_more:
        return self.empty_list(
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
        )

    last_id = getattr(self.data[-1], "id")
    if not last_id:
        raise ValueError(
            "Unexpected: element in .data of list object had no id"
        )

    params_with_filters = self._retrieve_params.copy()
    params_with_filters.update({"starting_after": last_id})
    params_with_filters.update(params)

    return await self.list(
        api_key=api_key,
        stripe_version=stripe_version,
        stripe_account=stripe_account,
        **params_with_filters
    )

async def previous_page_patch(
    self, api_key=None, stripe_version=None, stripe_account=None, **params
):
    if not self.has_more:
        return self.empty_list(
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
        )

    first_id = getattr(self.data[0], "id")
    if not first_id:
        raise ValueError(
            "Unexpected: element in .data of list object had no id"
        )

    params_with_filters = self._retrieve_params.copy()
    params_with_filters.update({"ending_before": first_id})
    params_with_filters.update(params)

    return await self.list(
        api_key=api_key,
        stripe_version=stripe_version,
        stripe_account=stripe_account,
        **params_with_filters
    )


stripe.ListObject.auto_paging_iter = auto_paging_iter_patch
stripe.ListObject.previous_page = previous_page_patch
stripe.ListObject.next_page = next_page_patch