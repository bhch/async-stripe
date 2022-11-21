# -*- coding: utf-8 -*-
import stripe
from stripe import util
from stripe import api_requestor
from stripe.six.moves.urllib.parse import quote_plus


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


stripe.Quote._cls_pdf = classmethod(_cls_pdf_patch)
stripe.Quote.pdf = pdf_patch
