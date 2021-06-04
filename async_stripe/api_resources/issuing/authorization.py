import stripe
from stripe import util
from async_stripe.api_resources.abstract import patch_custom_methods


async def approve_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/approve"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


async def decline_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/decline"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.issuing.Authorization.approve = approve_patch
stripe.issuing.Authorization.decline = decline_patch


custom_methods = [
    {"name": "approve", "http_verb": "post"},
    {"name": "decline", "http_verb": "post"},
]

patch_custom_methods(stripe.issuing.Authorization, custom_methods)