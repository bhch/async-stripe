import stripe
from stripe import util
from async_stripe.api_resources.abstract import patch_custom_methods


async def cancel_patch(self, idempotency_key=None, **params):
    url = "/v1/topups/{topup}/cancel".format(
        topup=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.Topup.cancel = cancel_patch


custom_methods = [
    {"name": "cancel", "http_verb": "post"},
]

patch_custom_methods(stripe.Topup, custom_methods)