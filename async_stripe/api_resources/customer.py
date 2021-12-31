import stripe
from async_stripe.api_resources.abstract import (
    patch_nested_resources, patch_custom_methods
)
from stripe import api_requestor
from stripe import util


async def delete_discount_patch(self, **params):
    requestor = api_requestor.APIRequestor(
        self.api_key,
        api_version=self.stripe_version,
        account=self.stripe_account,
    )
    url = self.instance_url() + "/discount"
    _, api_key = await requestor.request("delete", url, params)
    self.refresh_from({"discount": None}, api_key, True)

async def list_payment_methods_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/payment_methods"
    headers = util.populate_headers(idempotency_key)
    resp = await self.request("get", url, params, headers)
    stripe_object = util.convert_to_stripe_object(resp)
    stripe_object._retrieve_params = params
    return stripe_object

stripe.Customer.delete_discount = delete_discount_patch
stripe.Customer.list_payment_methods = list_payment_methods_patch


netsted_resources = ['balance_transaction', 'source', 'tax_id']
patch_nested_resources(stripe.Customer, netsted_resources)


# always patch custom methods after patching other methods
custom_resources = [
    {"name": "delete_discount", "http_verb": "delete", "http_path": "discount"},
    {"name": "list_payment_methods", "http_verb": "get", "http_path": "payment_methods"},
]
patch_custom_methods(stripe.Customer, custom_resources)
