from __future__ import absolute_import, division, print_function

import stripe
from stripe import api_requestor
from stripe import util


async def create_patch(
    # 'api_version' is deprecated, please use 'stripe_version'
    cls,
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
    url = cls.class_url()
    supplied_headers = {"Content-Type": "multipart/form-data"}
    response, api_key = await requestor.request(
        "post", url, params=params, headers=supplied_headers
    )
    return util.convert_to_stripe_object(
        response, api_key, version, stripe_account
    )


stripe.File.create = classmethod(create_patch)