import stripe
from async_stripe.api_resources.abstract import patch_custom_methods
from stripe import util


async def disconnect_patch(self, idempotency_key=None, **params):
    url = "/v1/financial_connections/accounts/{account}/disconnect".format(
        account=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self

async def refresh_account_patch(self, idempotency_key=None, **params):
    url = "/v1/financial_connections/accounts/{account}/refresh".format(
        account=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self

async def list_owners_patch(self, idempotency_key=None, **params):
    url = "/v1/financial_connections/accounts/{account}/owners".format(
        account=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    resp = await self.request("get", url, params, headers)
    stripe_object = util.convert_to_stripe_object(resp)
    stripe_object._retrieve_params = params
    return stripe_object


stripe.financial_connections.Account.disconnect = disconnect_patch
stripe.financial_connections.Account.refresh_account= refresh_account_patch
stripe.financial_connections.Account.list_owners = list_owners_patch


custom_resources = [
    {"name": "disconnect", "http_verb": "post", "http_path": "disconnect"},
    {"name": "refresh_account", "http_verb": "post", "http_path": "refresh"},
    {"name": "list_owners", "http_verb": "get", "http_path": "owners"},
]
patch_custom_methods(stripe.financial_connections.Account, custom_resources)
