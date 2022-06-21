import stripe
from stripe import api_requestor
from stripe import util


async def delete_where_patch(
    cls, api_key=None, stripe_version=None, stripe_account=None, **params
):
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    url = "/v1/apps/secrets/delete"
    response, api_key = await requestor.request("post", url, params)
    return util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )

async def find_patch(
    cls, api_key=None, stripe_version=None, stripe_account=None, **params
):
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    url = "/v1/apps/secrets/find"
    response, api_key = await requestor.request("get", url, params)
    return util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )


stripe.apps.Secret.delete_where = classmethod(delete_where_patch)
stripe.apps.Secret.find = classmethod(find_patch)