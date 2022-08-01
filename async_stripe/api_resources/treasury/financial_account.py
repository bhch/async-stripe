import stripe
from async_stripe.api_resources.abstract import patch_custom_methods
from stripe import util


async def retrieve_features_patch(self, idempotency_key=None, **params):
    url = "/v1/treasury/financial_accounts/{financial_account}/features".format(
        financial_account=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    resp = await self.request("get", url, params, headers)
    stripe_object = util.convert_to_stripe_object(resp)
    return stripe_object

async def update_features_patch(self, idempotency_key=None, **params):
    url = "/v1/treasury/financial_accounts/{financial_account}/features".format(
        financial_account=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    resp = await self.request("post", url, params, headers)
    stripe_object = util.convert_to_stripe_object(resp)
    return stripe_object


stripe.treasury.FinancialAccount.retrieve_features = retrieve_features_patch
stripe.treasury.FinancialAccount.update_features = update_features_patch


custom_resources = [
    {"name": "retrieve_features", "http_verb": "get", "http_path": "features"},
    {"name": "update_features", "http_verb": "post", "http_path": "features"},
]
patch_custom_methods(stripe.treasury.FinancialAccount, custom_resources)
