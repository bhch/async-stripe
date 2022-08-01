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
    url = "/v1/customers/{customer}/payment_methods".format(
        customer=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    resp = await self.request("get", url, params, headers)
    stripe_object = util.convert_to_stripe_object(resp)
    stripe_object._retrieve_params = params
    return stripe_object

async def create_funding_instructions_patch(self, idempotency_key=None, **params):
    url = "/v1/customers/{customer}/funding_instructions".format(
        customer=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    resp = await self.request("post", url, params, headers)
    stripe_object = util.convert_to_stripe_object(resp)
    return stripe_object

async def _cls_retrieve_payment_method_patch(
    cls,
    customer,
    payment_method,
    api_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    url = (
        "/v1/customers/{customer}/payment_methods/{payment_method}".format(
            customer=util.sanitize_id(customer),
            payment_method=util.sanitize_id(payment_method),
        )
    )
    response, api_key = await requestor.request("get", url, params)
    return util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )

@util.class_method_variant("_cls_retrieve_payment_method")
async def retrieve_payment_method_patch(
    self, payment_method, idempotency_key=None, **params
):
    url = (
        "/v1/customers/{customer}/payment_methods/{payment_method}".format(
            customer=util.sanitize_id(self.get("id")),
            payment_method=util.sanitize_id(payment_method),
        )
    )
    headers = util.populate_headers(idempotency_key)
    resp = await self.request("get", url, params, headers)
    stripe_object = util.convert_to_stripe_object(resp)
    return stripe_object

async def retrieve_cash_balance_patch(
    cls,
    customer,
    nested_id=None,
    api_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    # The nested_id parameter is required for backwards compatibility purposes and is ignored.
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    url = "/v1/customers/{customer}/cash_balance".format(
        customer=util.sanitize_id(customer)
    )
    response, api_key = await requestor.request("get", url, params)
    return util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )

async def modify_cash_balance_patch(
    cls,
    customer,
    nested_id=None,
    api_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    # The nested_id parameter is required for backwards compatibility purposes and is ignored.
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    url = "/v1/customers/{customer}/cash_balance".format(
        customer=util.sanitize_id(customer)
    )
    response, api_key = await requestor.request("post", url, params)
    return util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )


stripe.Customer.delete_discount = delete_discount_patch
stripe.Customer.list_payment_methods = list_payment_methods_patch
stripe.Customer._cls_retrieve_payment_method = classmethod(_cls_retrieve_payment_method_patch)
stripe.Customer.retrieve_payment_method = retrieve_payment_method_patch
stripe.Customer.retrieve_cash_balance = classmethod(retrieve_cash_balance_patch)
stripe.Customer.modify_cash_balance = classmethod(modify_cash_balance_patch)


netsted_resources = ['balance_transaction', 'source', 'tax_id']
patch_nested_resources(stripe.Customer, netsted_resources)


# always patch custom methods after patching other methods
custom_resources = [
    {"name": "delete_discount", "http_verb": "delete", "http_path": "discount"},
    {"name": "list_payment_methods", "http_verb": "get", "http_path": "payment_methods"},
    {"name": "create_funding_instructions", "http_verb": "post", "http_path": "funding_instructions"},
]
patch_custom_methods(stripe.Customer, custom_resources)


# methods for TestHelpers nested class
async def TestHelpers__cls_fund_cash_balance_patch(
    cls,
    customer,
    api_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    requestor = api_requestor.APIRequestor(
        api_key, api_version=stripe_version, account=stripe_account
    )
    url = "/v1/test_helpers/customers/{customer}/fund_cash_balance".format(
        customer=util.sanitize_id(customer)
    )
    response, api_key = await requestor.request("post", url, params)
    stripe_object = util.convert_to_stripe_object(
        response, api_key, stripe_version, stripe_account
    )
    return stripe_object

@util.class_method_variant("_cls_fund_cash_balance")
async def TestHelpers_fund_cash_balance_patch(self, idempotency_key=None, **params):
    url = "/v1/test_helpers/customers/{customer}/fund_cash_balance".format(
        customer=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.resource.refresh_from(
        await self.resource.request("post", url, params, headers)
    )
    return self.resource


stripe.Customer.TestHelpers._cls_fund_cash_balance = classmethod(TestHelpers__cls_fund_cash_balance_patch)
stripe.Customer.TestHelpers.fund_cash_balance = TestHelpers_fund_cash_balance_patch
