import stripe
from stripe import api_requestor
from stripe import util


# methods for TestHelpers nested class

async def create_patch(
    cls,
    api_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    url = "/v1/test_helpers/treasury/received_credits"
    response, api_key = await requestor.request("post", url, params)
    return util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )


stripe.treasury.ReceivedCredit.TestHelpers.create = classmethod(create_patch)
