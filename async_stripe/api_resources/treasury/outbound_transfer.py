import stripe
from stripe import util
from stripe import api_requestor
from async_stripe.api_resources.abstract import patch_custom_methods


async def cancel_patch(self, idempotency_key=None, **params):
    url = "/v1/treasury/outbound_transfers/{outbound_transfer}/cancel".format(
        outbound_transfer=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.treasury.OutboundTransfer.cancel = cancel_patch

custom_resources = [
    {"name": "cancel", "http_verb": "post"},
]
patch_custom_methods(stripe.treasury.OutboundTransfer, custom_resources)


# methods for TestHelpers nested class

async def TestHelpers__cls_fail_patch(
    cls,
    outbound_transfer,
    api_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    url = "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/fail".format(
        outbound_transfer=util.sanitize_id(outbound_transfer)
    )
    response, api_key = await requestor.request("post", url, params)
    stripe_object = util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )
    return stripe_object

@util.class_method_variant("_cls_fail")
async def TestHelpers_fail_patch(self, idempotency_key=None, **params):
    url = "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/fail".format(
        outbound_transfer=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource

async def TestHelpers__cls_post_patch(
    cls,
    outbound_transfer,
    api_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    url = "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/post".format(
        outbound_transfer=util.sanitize_id(outbound_transfer)
    )
    response, api_key = await requestor.request("post", url, params)
    stripe_object = util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )
    return stripe_object

@util.class_method_variant("_cls_post")
async def TestHelpers_post_patch(self, idempotency_key=None, **params):
    url = "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/post".format(
        outbound_transfer=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource

async def TestHelpers__cls_return_outbound_transfer_patch(
    cls,
    outbound_transfer,
    api_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    url = "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/return".format(
        outbound_transfer=util.sanitize_id(outbound_transfer)
    )
    response, api_key = await requestor.request("post", url, params)
    stripe_object = util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )
    return stripe_object

@util.class_method_variant("_cls_return_outbound_transfer")
async def TestHelpers_return_outbound_transfer_patch(self, idempotency_key=None, **params):
    url = "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/return".format(
        outbound_transfer=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource


stripe.treasury.OutboundTransfer.TestHelpers._cls_fail = classmethod(TestHelpers__cls_fail_patch)
stripe.treasury.OutboundTransfer.TestHelpers.fail = TestHelpers_fail_patch
stripe.treasury.OutboundTransfer.TestHelpers._cls_post = classmethod(TestHelpers__cls_post_patch)
stripe.treasury.OutboundTransfer.TestHelpers.post = TestHelpers_post_patch
stripe.treasury.OutboundTransfer.TestHelpers._cls_return_outbound_transfer = classmethod(TestHelpers__cls_return_outbound_transfer_patch)
stripe.treasury.OutboundTransfer.TestHelpers.return_outbound_transfer = TestHelpers_return_outbound_transfer_patch
