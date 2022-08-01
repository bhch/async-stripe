import stripe
from stripe import util
from stripe import api_requestor
from async_stripe.api_resources.abstract import patch_custom_methods


async def cancel_patch(self, idempotency_key=None, **params):
    url = "/v1/treasury/outbound_payments/{id}/cancel".format(
        id=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.treasury.OutboundPayment.cancel = cancel_patch

custom_resources = [
    {"name": "cancel", "http_verb": "post"},
]
patch_custom_methods(stripe.treasury.OutboundPayment, custom_resources)


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
        "/v1/test_helpers/treasury/outbound_payments/{id}/fail".format(
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
        "/v1/test_helpers/treasury/outbound_payments/{id}/fail".format(
            id=util.sanitize_id(self.get("id"))
        )
    )
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource

async def TestHelpers__cls_post_patch(
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
        "/v1/test_helpers/treasury/outbound_payments/{id}/post".format(
            id=util.sanitize_id(id)
        )
    )
    response, api_key = await requestor.request("post", url, params)
    stripe_object = util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )
    return stripe_object

@util.class_method_variant("_cls_post")
async def TestHelpers_post_patch(self, idempotency_key=None, **params):
    url = (
        "/v1/test_helpers/treasury/outbound_payments/{id}/post".format(
            id=util.sanitize_id(self.get("id"))
        )
    )
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource

async def TestHelpers__cls_return_outbound_payment_patch(
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
    url = "/v1/test_helpers/treasury/outbound_payments/{id}/return".format(
        id=util.sanitize_id(id)
    )
    response, api_key = await requestor.request("post", url, params)
    stripe_object = util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )
    return stripe_object

@util.class_method_variant("_cls_return_outbound_payment")
async def TestHelpers_return_outbound_payment_patch(self, idempotency_key=None, **params):
    url = "/v1/test_helpers/treasury/outbound_payments/{id}/return".format(
        id=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource


stripe.treasury.OutboundPayment.TestHelpers._cls_fail = classmethod(TestHelpers__cls_fail_patch)
stripe.treasury.OutboundPayment.TestHelpers.fail = TestHelpers_fail_patch
stripe.treasury.OutboundPayment.TestHelpers._cls_post = classmethod(TestHelpers__cls_post_patch)
stripe.treasury.OutboundPayment.TestHelpers.post = TestHelpers_post_patch
stripe.treasury.OutboundPayment.TestHelpers._cls_return_outbound_payment_patch = classmethod(TestHelpers__cls_return_outbound_payment_patch)
stripe.treasury.OutboundPayment.TestHelpers.return_outbound_payment = TestHelpers_return_outbound_payment_patch
