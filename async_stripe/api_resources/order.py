import stripe
from stripe import util
from async_stripe.api_resources.abstract import patch_custom_methods


async def pay_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/pay"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self

async def cancel_patch(self, idempotency_key=None, **params):
    url = "/v1/orders/{id}/cancel".format(
        id=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self

async def list_line_items_patch(self, idempotency_key=None, **params):
    url = "/v1/orders/{id}/line_items".format(
        id=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    resp = await self.request("get", url, params, headers)
    stripe_object = util.convert_to_stripe_object(resp)
    stripe_object._retrieve_params = params
    return stripe_object

async def reopen_patch(self, idempotency_key=None, **params):
    url = "/v1/orders/{id}/reopen".format(
        id=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self

async def submit_patch(self, idempotency_key=None, **params):
    url = "/v1/orders/{id}/submit".format(
        id=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.Order.cancel = cancel_patch
stripe.Order.list_line_items = list_line_items_patch
stripe.Order.reopen = reopen_patch
stripe.Order.submit = submit_patch


custom_methods = [
    {"name": "cancel", "http_verb": "post"},
    {"name": "list_line_items", "http_verb": "get", "http_path": "line_items"},
    {"name": "reopen", "http_verb": "post"},
    {"name": "submit", "http_verb": "post"},
]

patch_custom_methods(stripe.Order, custom_methods)
