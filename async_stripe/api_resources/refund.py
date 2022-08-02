import stripe
from stripe import util
from stripe import api_requestor
from async_stripe.api_resources.abstract import patch_custom_methods


async def cancel_patch(self, idempotency_key=None, **params):
    url = "/v1/refunds/{refund}/cancel".format(
        refund=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.Refund.cancel = cancel_patch


custom_resources = [
    {"name": "cancel", "http_verb": "post"}
]
patch_custom_methods(stripe.Refund, custom_resources)


# methods for TestHelpers nested class
async def TestHelpers__cls_expire_patch(
    cls,
    refund,
    api_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    url = "/v1/test_helpers/refunds/{refund}/expire".format(
        refund=util.sanitize_id(refund)
    )
    response, api_key = await requestor.request("post", url, params)
    stripe_object = util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )
    return stripe_object

@util.class_method_variant("_cls_expire")
async def TestHelpers_expire_patch(self, idempotency_key=None, **params):
    url = "/v1/test_helpers/refunds/{refund}/expire".format(
        refund=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource


stripe.Refund.TestHelpers._cls_expire = classmethod(TestHelpers__cls_expire_patch)
stripe.Refund.TestHelpers.expire = TestHelpers_expire_patch
