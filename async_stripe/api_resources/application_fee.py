import stripe
from stripe import util
from stripe.api_resources.abstract import ListableAPIResource
from async_stripe.api_resources.abstract import patch_nested_resources


async def refund_patch(self, idempotency_key=None, **params):
    headers = util.populate_headers(idempotency_key)
    url = self.instance_url() + "/refund"
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.ApplicationFee.refund = refund_patch


nested_resources = ["refund"]

patch_nested_resources(stripe.ApplicationFee, nested_resources)