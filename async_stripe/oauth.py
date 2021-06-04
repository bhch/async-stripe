import stripe
from stripe import api_requestor, connect_api_base


async def token_patch(api_key=None, **params):
    requestor = api_requestor.APIRequestor(
        api_key, api_base=connect_api_base
    )
    response, _ = await requestor.request("post", "/oauth/token", params, None)
    return response.data


async def deauthorize_patch(api_key=None, **params):
    requestor = api_requestor.APIRequestor(
        api_key, api_base=connect_api_base
    )
    stripe.OAuth._set_client_id(params)
    response, _ = await requestor.request(
        "post", "/oauth/deauthorize", params, None
    )
    return response.data


stripe.OAuth.token = staticmethod(token_patch)
stripe.OAuth.deauthorize = staticmethod(deauthorize_patch)