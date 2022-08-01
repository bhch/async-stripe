import stripe
from stripe import util
from async_stripe.api_resources.abstract import patch_custom_methods


async def cancel_patch(self, idempotency_key=None, **params):
    url = "/v1/payouts/{payout}/cancel".format(
        payout=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


async def reverse_patch(self, idempotency_key=None, **params):
    url = "/v1/payouts/{payout}/reverse".format(
        payout=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.Payout.cancel = cancel_patch
stripe.Payout.reverse = reverse_patch


custom_methods = [
    {"name": "cancel", "http_verb": "post"},
    {"name": "reverse", "http_verb": "post"},
]

patch_custom_methods(stripe.Payout, custom_methods)
