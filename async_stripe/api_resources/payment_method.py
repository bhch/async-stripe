import stripe
from stripe import util
from async_stripe.api_resources.abstract import patch_custom_methods


async def attach_patch(self, idempotency_key=None, **params):
    url = "/v1/payment_methods/{payment_method}/attach".format(
        payment_method=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


async def detach_patch(self, idempotency_key=None, **params):
    url = "/v1/payment_methods/{payment_method}/detach".format(
        payment_method=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.PaymentMethod.attach = attach_patch
stripe.PaymentMethod.detach = detach_patch


custom_methods = [
    {"name": "attach", "http_verb": "post"},
    {"name": "detach", "http_verb": "post"},
]

patch_custom_methods(stripe.PaymentMethod, custom_methods)