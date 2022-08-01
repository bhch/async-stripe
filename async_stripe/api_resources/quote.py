import stripe
from stripe import util
from stripe import api_requestor
from stripe.six.moves.urllib.parse import quote_plus
from async_stripe.api_resources.abstract import patch_custom_methods


async def accept_patch(self, idempotency_key=None, **params):
    url = "/v1/quotes/{quote}/accept".format(
        quote=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self

async def cancel_patch(self, idempotency_key=None, **params):
    url = "/v1/quotes/{quote}/cancel".format(
        quote=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self

async def finalize_quote_patch(self, idempotency_key=None, **params):
    url = "/v1/quotes/{quote}/finalize".format(
        quote=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self

async def list_computed_upfront_line_items_patch(self, idempotency_key=None, **params):
    url = "/v1/quotes/{quote}/computed_upfront_line_items".format(
        quote=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    resp = await self.request("get", url, params, headers)
    stripe_object = util.convert_to_stripe_object(resp)
    stripe_object._retrieve_params = params
    return stripe_object

async def list_line_items_patch(self, idempotency_key=None, **params):
    url = "/v1/quotes/{quote}/line_items".format(
        quote=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    resp = await self.request("get", url, params, headers)
    stripe_object = util.convert_to_stripe_object(resp)
    stripe_object._retrieve_params = params
    return stripe_object

async def _cls_pdf_patch(
    cls,
    sid,
    api_key=None,
    idempotency_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    url = "%s/%s/%s" % (
        cls.class_url(),
        quote_plus(util.utf8(sid)),
        "pdf",
    )
    requestor = api_requestor.APIRequestor(
        api_key,
        api_base=stripe.upload_api_base,
        api_version=stripe_version,
        account=stripe_account,
    )
    headers = util.populate_headers(idempotency_key)
    response, _ = await requestor.request_stream("get", url, params, headers)
    return response

@util.class_method_variant("_cls_pdf")
async def pdf_patch(
    self,
    api_key=None,
    api_version=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    version = api_version or stripe_version
    requestor = api_requestor.APIRequestor(
        api_key,
        api_base=stripe.upload_api_base,
        api_version=version,
        account=stripe_account,
    )
    url = self.instance_url() + "/pdf"
    return await requestor.request_stream("get", url, params=params)


stripe.Quote.accept = accept_patch
stripe.Quote.cancel = cancel_patch
stripe.Quote.finalize_quote = finalize_quote_patch
stripe.Quote.list_computed_upfront_line_items = list_computed_upfront_line_items_patch
stripe.Quote.list_line_items = list_line_items_patch
stripe.Quote._cls_pdf = classmethod(_cls_pdf_patch)
stripe.Quote.pdf = pdf_patch


custom_resources = [
    {"name": "accept", "http_verb": "post"},
    {"name": "cancel", "http_verb": "post"},
    {"name": "finalize_quote", "http_verb": "post", "http_path": "finalize"},
    {"name": "list_computed_upfront_line_items", "http_verb": "get", "http_path": "computed_upfront_line_items"},
    {"name": "list_line_items", "http_verb": "get", "http_path": "line_items"},
]
patch_custom_methods(stripe.Quote, custom_resources)
