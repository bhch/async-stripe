import stripe
from async_stripe.api_resources.abstract import patch_custom_methods
from stripe import util


async def disconnect_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/disconnect"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self

async def refresh_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/refresh"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.financial_connections.Account.disconnect = disconnect_patch
stripe.financial_connections.Account.refresh = refresh_patch


custom_resources = [
    {"name": "disconnect", "http_verb": "post", "http_path": "disconnect"},
    {"name": "refresh", "http_verb": "post", "http_path": "refresh"},
]
patch_custom_methods(stripe.financial_connections.Account, custom_resources)
