import stripe
from async_stripe.api_resources.abstract import patch_custom_methods
from stripe import util


async def cancel_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/cancel"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.treasury.OutboundPayment.cancel = cancel_patch

custom_resources = [
    {"name": "cancel", "http_verb": "post"},
]
patch_custom_methods(stripe.treasury.OutboundPayment, custom_resources)


# methods for TestHelpers nested class

async def fail_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/fail"
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource

async def post_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/post"
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource

async def return_outbound_payment_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/return"
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource


stripe.treasury.OutboundPayment.TestHelpers.fail = fail_patch
stripe.treasury.OutboundPayment.TestHelpers.post = post_patch
stripe.treasury.OutboundPayment.TestHelpers.return_outbound_payment = return_outbound_payment_patch


TestHelpers_custom_resources = [
    {"name": "fail", "http_verb": "post"},
    {"name": "post", "http_verb": "post"},
    {"name": "return_outbound_payment", "http_verb": "post", "http_path": "post"},
]
patch_custom_methods(stripe.treasury.OutboundPayment.TestHelpers, TestHelpers_custom_resources)
