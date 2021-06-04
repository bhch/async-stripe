import stripe
from stripe import util
from async_stripe.api_resources.abstract import patch_custom_methods


async def attach_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/attach"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


async def detach_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/detach"
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