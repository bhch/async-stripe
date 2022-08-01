import stripe
from stripe import util
from async_stripe.api_resources.abstract import patch_custom_methods


async def list_line_items_patch(self, idempotency_key=None, **params):
    url = "/v1/payment_links/{payment_link}/line_items".format(
        payment_link=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    resp = await self.request("get", url, params, headers)
    stripe_object = util.convert_to_stripe_object(resp)
    stripe_object._retrieve_params = params
    return stripe_object


stripe.PaymentLink.list_line_items = list_line_items_patch


custom_resources = [
    {"name": "list_line_items", "http_verb": "get", "http_path": "line_items"},
]
patch_custom_methods(stripe.PaymentLink, custom_resources)
