import stripe
from stripe import util
from stripe import api_requestor
from async_stripe.api_resources.abstract import patch_custom_methods


async def cancel_patch(self, idempotency_key=None, **params):
    url = (
        "/v1/treasury/inbound_transfers/{inbound_transfer}/cancel".format(
            inbound_transfer=util.sanitize_id(self.get("id"))
        )
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.treasury.InboundTransfer.cancel = cancel_patch


custom_resources = [
    {"name": "cancel", "http_verb": "post"},
]
patch_custom_methods(stripe.treasury.InboundTransfer, custom_resources)


# methods for TestHelpers nested class

async def TestHelpers__cls_fail_patch(
    cls,
    id,
    api_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    url = (
        "/v1/test_helpers/treasury/inbound_transfers/{id}/fail".format(
            id=util.sanitize_id(id)
        )
    )
    response, api_key = await requestor.request("post", url, params)
    stripe_object = util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )
    return stripe_object

@util.class_method_variant("_cls_fail")
async def TestHelpers_fail_patch(self, idempotency_key=None, **params):
    url = (
        "/v1/test_helpers/treasury/inbound_transfers/{id}/fail".format(
            id=util.sanitize_id(self.get("id"))
        )
    )
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource

async def TestHelpers__cls_return_inbound_transfer_patch(
    cls,
    id,
    api_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    url = "/v1/test_helpers/treasury/inbound_transfers/{id}/return".format(
        id=util.sanitize_id(id)
    )
    response, api_key = await requestor.request("post", url, params)
    stripe_object = util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )
    return stripe_object

@util.class_method_variant("_cls_return_inbound_transfer")
async def TestHelpers_return_inbound_transfer_patch(self, idempotency_key=None, **params):
    url = "/v1/test_helpers/treasury/inbound_transfers/{id}/return".format(
        id=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource

async def TestHelpers__cls_succeed_patch(
    cls,
    id,
    api_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    url = "/v1/test_helpers/treasury/inbound_transfers/{id}/succeed".format(
        id=util.sanitize_id(id)
    )
    response, api_key = await requestor.request("post", url, params)
    stripe_object = util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )
    return stripe_object

@util.class_method_variant("_cls_succeed")
async def TestHelpers_succeed_patch(self, idempotency_key=None, **params):
    url = "/v1/test_helpers/treasury/inbound_transfers/{id}/succeed".format(
        id=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource


stripe.treasury.InboundTransfer.TestHelpers._cls_fail = classmethod(TestHelpers__cls_fail_patch)
stripe.treasury.InboundTransfer.TestHelpers.fail = TestHelpers_fail_patch
stripe.treasury.InboundTransfer.TestHelpers._cls_return_inbound_transfer = classmethod(TestHelpers__cls_return_inbound_transfer_patch)
stripe.treasury.InboundTransfer.TestHelpers.return_inbound_transfer = TestHelpers_return_inbound_transfer_patch
stripe.treasury.InboundTransfer.TestHelpers._cls_succeed = classmethod(TestHelpers__cls_succeed_patch)
stripe.treasury.InboundTransfer.TestHelpers.succeed = TestHelpers_succeed_patch
