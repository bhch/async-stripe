import stripe
from stripe import util
from async_stripe.api_resources.abstract import patch_custom_methods


async def cancel_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/cancel"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


async def capture_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/capture"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


async def confirm_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/confirm"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


async def verify_microdeposits_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/verify_microdeposits"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


async def apply_customer_balance_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/apply_customer_balance"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


async def increment_authorization_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/increment_authorization"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.PaymentIntent.cancel = cancel_patch
stripe.PaymentIntent.capture = capture_patch
stripe.PaymentIntent.confirm = confirm_patch
stripe.PaymentIntent.verify_microdeposits = verify_microdeposits_patch
stripe.PaymentIntent.apply_customer_balance = apply_customer_balance_patch
stripe.PaymentIntent.increment_authorization = increment_authorization_patch


custom_resources = [
    {"name": "cancel", "http_verb": "post"},
    {"name": "capture", "http_verb": "post"},
    {"name": "confirm", "http_verb": "post"},
    {"name": "verify_microdeposits", "http_verb": "post"},
    {"name": "apply_customer_balance", "http_verb": "post"},
    {"name": "increment_authorization", "http_verb": "post"},
]
patch_custom_methods(stripe.PaymentIntent, custom_resources)
