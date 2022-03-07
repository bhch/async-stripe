import stripe
from stripe import util
from async_stripe.api_resources.abstract import patch_custom_methods


async def advance_patch(self, idempotency_key=None, **params):
        url = self.instance_url() + "/advance"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(await self.request("post", url, params, headers))
        return self


stripe.test_helpers.TestClock.advance = advance_patch


custom_methods = [
    {"name": "advance", "http_verb": "post"},
]

patch_custom_methods(stripe.test_helpers.TestClock, custom_methods)
