import stripe
from stripe import util
from async_stripe.api_resources.abstract import patch_custom_methods


async def cancel_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/cancel"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


async def confirm_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/confirm"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.SetupIntent.cancel = cancel_patch
stripe.SetupIntent.confirm = confirm_patch


custom_methods = [
    {"name": "cancel", "http_verb": "post"},
    {"name": "confirm", "http_verb": "post"},
]

patch_custom_methods(stripe.SetupIntent, custom_methods)