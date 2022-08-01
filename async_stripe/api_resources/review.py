import stripe
from stripe import util
from async_stripe.api_resources.abstract import patch_custom_methods


async def approve_patch(self, idempotency_key=None, **params):
    url = "/v1/reviews/{review}/approve".format(
        review=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.Review.approve = approve_patch


custom_methods = [
    {"name": "approve", "http_verb": "post"},
]

patch_custom_methods(stripe.Review, custom_methods)