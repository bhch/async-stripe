import stripe
from async_stripe.api_resources.abstract import patch_custom_methods
from stripe import util


async def cancel_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/cancel"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.treasury.InboundTransfer.cancel = cancel_patch


custom_resources = [
    {"name": "cancel", "http_verb": "post"},
]
patch_custom_methods(stripe.treasury.InboundTransfer, custom_resources)


# methods for TestHelpers nested class

async def fail_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/fail"
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource

async def return_inbound_transfer_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/return"
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource

async def succeed_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/succeed"
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource


stripe.treasury.InboundTransfer.TestHelpers.fail = fail_patch
stripe.treasury.InboundTransfer.TestHelpers.return_inbound_transfer = return_inbound_transfer_patch
stripe.treasury.InboundTransfer.TestHelpers.succeed = succeed_patch


TestHelpers_custom_resources = [
    {"name": "fail", "http_verb": "post"},
    {"name": "return_inbound_transfer", "http_verb": "post", "http_path": "return"},
    {"name": "succeed", "http_verb": "post"},
]
patch_custom_methods(stripe.treasury.InboundTransfer.TestHelpers, TestHelpers_custom_resources)
