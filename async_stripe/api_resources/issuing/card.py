import stripe
from stripe import api_requestor
from stripe import util
from async_stripe.api_resources.abstract import patch_custom_methods



async def details_patch(self, idempotency_key=None, **params):
    return await self.request("get", self.instance_url() + "/details", params)


stripe.issuing.Card.details = details_patch


custom_methods = [
    {"name": "details", "http_verb": "get"}
]

patch_custom_methods(stripe.issuing.Card, custom_methods)


# TestHelpers

async def TestHelpers__cls_deliver_card_patch(
    cls,
    card,
    api_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    url = "/v1/test_helpers/issuing/cards/{card}/shipping/deliver".format(
        card=util.sanitize_id(card)
    )
    response, api_key = await requestor.request("post", url, params)
    stripe_object = util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )
    return stripe_object

@util.class_method_variant("_cls_deliver_card")
async def TestHelpers_deliver_card_patch(self, idempotency_key=None, **params):
    url = "/v1/test_helpers/issuing/cards/{card}/shipping/deliver".format(
        card=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource

async def TestHelpers__cls_fail_card_patch(
    cls,
    card,
    api_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    url = "/v1/test_helpers/issuing/cards/{card}/shipping/fail".format(
        card=util.sanitize_id(card)
    )
    response, api_key = await requestor.request("post", url, params)
    stripe_object = util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )
    return stripe_object

@util.class_method_variant("_cls_fail_card")
async def TestHelpers_fail_card_patch(self, idempotency_key=None, **params):
    url = "/v1/test_helpers/issuing/cards/{card}/shipping/fail".format(
        card=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource

async def TestHelpers__cls_return_card_patch(
    cls,
    card,
    api_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    url = (
        "/v1/test_helpers/issuing/cards/{card}/shipping/return".format(
            card=util.sanitize_id(card)
        )
    )
    response, api_key = await requestor.request("post", url, params)
    stripe_object = util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )
    return stripe_object

@util.class_method_variant("_cls_return_card")
async def TestHelpers_return_card_patch(self, idempotency_key=None, **params):
    url = (
        "/v1/test_helpers/issuing/cards/{card}/shipping/return".format(
            card=util.sanitize_id(self.get("id"))
        )
    )
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource

async def TestHelpers__cls_ship_card_patch(
    cls,
    card,
    api_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    url = "/v1/test_helpers/issuing/cards/{card}/shipping/ship".format(
        card=util.sanitize_id(card)
    )
    response, api_key = await requestor.request("post", url, params)
    stripe_object = util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )
    return stripe_object

@util.class_method_variant("_cls_ship_card")
async def TestHelpers_ship_card_patch(self, idempotency_key=None, **params):
    url = "/v1/test_helpers/issuing/cards/{card}/shipping/ship".format(
        card=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource


stripe.issuing.Card.TestHelpers._cls_deliver_card = classmethod(TestHelpers__cls_deliver_card_patch)
stripe.issuing.Card.TestHelpers.deliver_card = TestHelpers_deliver_card_patch
stripe.issuing.Card.TestHelpers._cls_fail_card = classmethod(TestHelpers__cls_fail_card_patch)
stripe.issuing.Card.TestHelpers.fail_card = TestHelpers_fail_card_patch
stripe.issuing.Card.TestHelpers._cls_return_card = classmethod(TestHelpers__cls_return_card_patch)
stripe.issuing.Card.TestHelpers.return_card = TestHelpers_return_card_patch
stripe.issuing.Card.TestHelpers._cls_ship_card = classmethod(TestHelpers__cls_ship_card_patch)
stripe.issuing.Card.TestHelpers.ship_card = TestHelpers_ship_card_patch
