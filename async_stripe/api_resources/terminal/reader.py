import stripe
from stripe import util
from stripe import api_requestor
from async_stripe.api_resources.abstract import patch_custom_methods


async def cancel_action_patch(self, idempotency_key=None, **params):
    url = "/v1/terminal/readers/{reader}/cancel_action".format(
        reader=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self

async def process_payment_intent_patch(self, idempotency_key=None, **params):
    url = "/v1/terminal/readers/{reader}/process_payment_intent".format(
        reader=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self

async def process_setup_intent_patch(self, idempotency_key=None, **params):
    url = "/v1/terminal/readers/{reader}/process_setup_intent".format(
        reader=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self

async def set_reader_display_patch(self, idempotency_key=None, **params):
    url = "/v1/terminal/readers/{reader}/set_reader_display".format(
        reader=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.terminal.Reader.cancel_action = cancel_action_patch
stripe.terminal.Reader.process_payment_intent = process_setup_intent_patch
stripe.terminal.Reader.process_setup_intent = process_setup_intent_patch
stripe.terminal.Reader.set_reader_display = set_reader_display_patch


custom_resources = [
    {"name": "cancel_action", "http_verb": "post"},
    {"name": "process_payment_intent", "http_verb": "post"},
    {"name": "process_setup_intent", "http_verb": "post"},
    {"name": "set_reader_display", "http_verb": "post"},
]
patch_custom_methods(stripe.terminal.Reader, custom_resources)


# methods for TestHelpers class (nested inside Reader class)
async def TestHelpers__cls_present_payment_method_patch(
    cls,
    reader,
    api_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    url = "/v1/test_helpers/terminal/readers/{reader}/present_payment_method".format(
        reader=util.sanitize_id(reader)
    )
    response, api_key = await requestor.request("post", url, params)
    stripe_object = util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )
    return stripe_object

@util.class_method_variant("_cls_present_payment_method")
async def TestHelpers_present_payment_method_patch(self, idempotency_key=None, **params):
    url = "/v1/test_helpers/terminal/readers/{reader}/present_payment_method".format(
        reader=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource


stripe.terminal.Reader.TestHelpers._cls_present_payment_method = classmethod(TestHelpers__cls_present_payment_method_patch)
stripe.terminal.Reader.TestHelpers.present_payment_method = TestHelpers_present_payment_method_patch
