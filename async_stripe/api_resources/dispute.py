import stripe
from stripe import util
from async_stripe.api_resources.abstract import patch_custom_methods


async def close_patch(self, idempotency_key=None, **params):
    url = "/v1/disputes/{dispute}/close".format(
        dispute=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.Dispute.close = close_patch


custom_methods = [
    {"name": "close", "http_verb": "post"}
]

patch_custom_methods(stripe.Dispute, custom_methods)