import stripe
from async_stripe.api_resources.abstract import patch_custom_methods


async def details_patch(self, idempotency_key=None, **params):
    return await self.request("get", self.instance_url() + "/details", params)


stripe.issuing.Card.details = details_patch


custom_methods = [
    {"name": "details", "http_verb": "get"}
]

patch_custom_methods(stripe.issuing.Card, custom_methods)