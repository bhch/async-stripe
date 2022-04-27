import stripe
from stripe import util
from async_stripe.api_resources.abstract import patch_custom_methods


async def cancel_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/cancel"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.Refund.cancel = cancel_patch


custom_resources = [
    {"name": "cancel", "http_verb": "post"}
]
patch_custom_methods(stripe.Refund, custom_resources)


# methods for TestHelpers nested class
async def TestHelpers_expire_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/expire"
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        self.resource.request("post", url, params, headers)
    )
    return self.resource


stripe.Refund.TestHelpers.expire = TestHelpers_expire_patch


TestHelpers_custom_resources = [
    {"name": "expire", "http_verb": "post"}
]
patch_custom_methods(stripe.Refund.TestHelpers, TestHelpers_custom_resources)
