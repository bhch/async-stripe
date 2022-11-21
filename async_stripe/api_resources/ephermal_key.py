# -*- coding: utf-8 -*-
import stripe
from stripe import api_requestor
from stripe import util


async def create_patch(
    cls,
    api_key=None,
    idempotency_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    if stripe_version is None:
        raise ValueError(
            "stripe_version must be specified to create an ephemeral "
            "key"
        )

    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )

    url = cls.class_url()
    headers = util.populate_headers(idempotency_key)
    response, api_key = await requestor.request("post", url, params, headers)
    return util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )


stripe.EphemeralKey.create = classmethod(create_patch)