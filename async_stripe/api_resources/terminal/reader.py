import stripe
from stripe import util
from async_stripe.api_resources.abstract import patch_custom_methods


async def cancel_action_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/cancel_action"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self

async def process_payment_intent_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/process_payment_intent"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self

async def process_setup_intent_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/process_setup_intent"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self

async def set_reader_display_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/set_reader_display"
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
async def TestHelpers_present_payment_method_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/present_payment_method"
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource


stripe.terminal.Reader.TestHelpers.present_payment_method = TestHelpers_present_payment_method_patch


TestHelpers_custom_resources = [
    {"name": "present_payment_method", "http_verb": "post"}
]
patch_custom_methods(stripe.terminal.Reader.TestHelpers, TestHelpers_custom_resources)
