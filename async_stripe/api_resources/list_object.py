import stripe
from stripe import api_requestor, six, util
from stripe.stripe_object import StripeObject

from stripe.six.moves.urllib.parse import quote_plus


async def list_patch(
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

async def create_patch(
    self,
    api_key=None,
    idempotency_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    return await self._request(
        "post",
        self.get("url"),
        api_key=api_key,
        idempotency_key=idempotency_key,
        stripe_version=stripe_version,
        stripe_account=stripe_account,
        **params
    )

async def retrieve_patch(
    self,
    id,
    api_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    url = "%s/%s" % (self.get("url"), quote_plus(util.utf8(id)))
    return await self._request(
        "get",
        url,
        api_key=api_key,
        stripe_version=stripe_version,
        stripe_account=stripe_account,
        **params
    )

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

    last_id = self.data[-1].id

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

    first_id = self.data[0].id

    params_with_filters = self._retrieve_params.copy()
    params_with_filters.update({"ending_before": first_id})
    params_with_filters.update(params)

    return await self.list(
        api_key=api_key,
        stripe_version=stripe_version,
        stripe_account=stripe_account,
        **params_with_filters
    )


stripe.ListObject.list = list_patch
stripe.ListObject.create = create_patch
stripe.ListObject.retrieve = retrieve_patch
stripe.ListObject._request = _request_patch
stripe.ListObject.auto_paging_iter = auto_paging_iter_patch
stripe.ListObject.previous_page = previous_page_patch
stripe.ListObject.next_page = next_page_patch