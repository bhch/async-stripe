import stripe
from stripe import api_requestor
from stripe import util
from async_stripe.api_resources.abstract import patch_custom_methods


async def void_credit_note_patch(self, idempotency_key=None, **params):
    url = "/v1/credit_notes/{id}/void".format(
        id=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


async def preview_patch(
    cls, api_key=None, stripe_version=None, stripe_account=None, **params
):
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    url = cls.class_url() + "/preview"
    response, api_key = await requestor.request("get", url, params)
    return util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )


stripe.CreditNote.void_credit_note = void_credit_note_patch
stripe.CreditNote.preview = classmethod(preview_patch)


custom_methods = [
    {"name": "void_credit_note", "http_verb": "post", "http_path": "void"},
]

patch_custom_methods(stripe.CreditNote, custom_methods)