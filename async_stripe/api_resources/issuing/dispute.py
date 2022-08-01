import stripe
from stripe import util
from async_stripe.api_resources.abstract import patch_custom_methods


async def submit_patch(self, idempotency_key=None, **params):
    url = "/v1/issuing/disputes/{dispute}/submit".format(
        dispute=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.issuing.Dispute.submit = submit_patch


custom_methods = [
    {"name": "submit", "http_verb": "post"}
]

patch_custom_methods(stripe.issuing.Dispute, custom_methods)