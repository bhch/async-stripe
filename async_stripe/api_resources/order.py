import stripe
from stripe import util
from async_stripe.api_resources.abstract import patch_custom_methods


async def pay_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/pay"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


async def return_order_patch(self, idempotency_key=None, **params):
    headers = util.populate_headers(idempotency_key)
    return await self.request(
        "post", self.instance_url() + "/returns", params, headers
    )


stripe.Order.pay = pay_patch
stripe.Order.return_order = return_order_patch


custom_methods = [
    {"name": "pay", "http_verb": "post"},
    {"name": "return_order", "http_verb": "post", "http_path": "returns"},
]

patch_custom_methods(stripe.Order, custom_methods)