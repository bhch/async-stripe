import stripe
from stripe import util
from async_stripe.api_resources.abstract import patch_custom_methods


async def cancel_patch(self, idempotency_key=None, **params):
    url = "/v1/subscription_schedules/{schedule}/cancel".format(
        schedule=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


async def release_patch(self, idempotency_key=None, **params):
    url = "/v1/subscription_schedules/{schedule}/release".format(
        schedule=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.SubscriptionSchedule.cancel = cancel_patch
stripe.SubscriptionSchedule.release = release_patch


custom_methods = [
    {"name": "cancel", "http_verb": "post"},
    {"name": "release", "http_verb": "post"},
]

patch_custom_methods(stripe.SubscriptionSchedule, custom_methods)