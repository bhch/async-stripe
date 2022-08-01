import stripe
from stripe import util
from async_stripe.api_resources.abstract import patch_custom_methods, patch_nested_resources


async def expire_patch(self, idempotency_key=None, **params):
    url = "/v1/checkout/sessions/{session}/expire".format(
        session=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.checkout.Session.expire = expire_patch


custom_resources = [
    {"name": "expire", "http_verb": "post"},
]
patch_custom_methods(stripe.checkout.Session, custom_resources)


nested_resources = ["line_item"]
patch_nested_resources(stripe.checkout.Session, nested_resources)