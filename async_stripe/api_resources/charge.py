import stripe
from stripe import api_requestor
from stripe import util
from async_stripe.api_resources.abstract import patch_custom_methods


async def capture_patch(self, idempotency_key=None, **params):
    url = "/v1/charges/{charge}/capture".format(
        charge=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self

async def refund_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/refund"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self

async def update_dispute_patch(self, idempotency_key=None, **params):
    requestor = api_requestor.APIRequestor(
        self.api_key,
        api_version=self.stripe_version,
        account=self.stripe_account,
    )
    url = self.instance_url() + "/dispute"
    headers = util.populate_headers(idempotency_key)
    response, api_key = await requestor.request("post", url, params, headers)
    self.refresh_from({"dispute": response}, api_key, True)
    return self.dispute

async def close_dispute_patch(self, idempotency_key=None, **params):
    requestor = api_requestor.APIRequestor(
        self.api_key,
        api_version=self.stripe_version,
        account=self.stripe_account,
    )
    url = self.instance_url() + "/dispute/close"
    headers = util.populate_headers(idempotency_key)
    response, api_key = await requestor.request("post", url, params, headers)
    self.refresh_from({"dispute": response}, api_key, True)
    return self.dispute

async def mark_as_fraudulent_patch(self, idempotency_key=None):
    params = {"fraud_details": {"user_report": "fraudulent"}}
    url = self.instance_url()
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self

async def mark_as_safe_patch(self, idempotency_key=None):
    params = {"fraud_details": {"user_report": "safe"}}
    url = self.instance_url()
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.Charge.capture = capture_patch
stripe.Charge.refund = refund_patch
stripe.Charge.update_dispute = update_dispute_patch
stripe.Charge.close_dispute = close_dispute_patch
stripe.Charge.mark_as_fraudulent = mark_as_fraudulent_patch
stripe.Charge.mark_as_safe = mark_as_safe_patch


custom_methods = [
    {"name": "capture", "http_verb": "post"},
]

patch_custom_methods(stripe.Charge, custom_methods)