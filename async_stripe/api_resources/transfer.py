import stripe
from stripe import util
from async_stripe.api_resources.abstract import (
    patch_custom_methods, patch_nested_resources
)


async def cancel_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/cancel"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.Transfer.cancel = cancel_patch


netsted_resources = ["reversal"]
patch_nested_resources(stripe.Transfer, netsted_resources)


custom_methods = [
    {"name": "cancel", "http_verb": "post"}
]
patch_custom_methods(stripe.Transfer, custom_methods)