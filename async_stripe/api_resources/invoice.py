import stripe
from stripe import api_requestor
from stripe import util
from async_stripe.api_resources.abstract import patch_custom_methods


async def finalize_invoice_patch(self, idempotency_key=None, **params):
    url = "/v1/invoices/{invoice}/finalize".format(
        invoice=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


async def mark_uncollectible_patch(self, idempotency_key=None, **params):
    url = "/v1/invoices/{invoice}/mark_uncollectible".format(
        invoice=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


async def pay_patch(self, idempotency_key=None, **params):
    url = "/v1/invoices/{invoice}/pay".format(
        invoice=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


async def send_invoice_patch(self, idempotency_key=None, **params):
    url = "/v1/invoices/{invoice}/send".format(
        invoice=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


async def void_invoice_patch(self, idempotency_key=None, **params):
    url = "/v1/invoices/{invoice}/void".format(
        invoice=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


async def upcoming_patch(
    cls, api_key=None, stripe_version=None, stripe_account=None, **params
):
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    url = cls.class_url() + "/upcoming"
    response, api_key = await requestor.request("get", url, params)
    return util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )


stripe.Invoice.finalize_invoice = finalize_invoice_patch
stripe.Invoice.mark_uncollectible = mark_uncollectible_patch
stripe.Invoice.pay = pay_patch
stripe.Invoice.send_invoice = send_invoice_patch
stripe.Invoice.void_invoice = void_invoice_patch
stripe.Invoice.upcoming = classmethod(upcoming_patch)


custom_methods = [
    {"name": "finalize_invoice", "http_verb": "post", "http_path": "finalize"},
    {"name": "mark_uncollectible", "http_verb": "post"},
    {"name": "pay", "http_verb": "post"},
    {"name": "send_invoice", "http_verb": "post", "http_path": "send"},
    {"name": "void_invoice", "http_verb": "post", "http_path": "void"},
]


patch_custom_methods(stripe.Invoice, custom_methods)
