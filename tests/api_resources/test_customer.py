from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "cus_123"
TEST_SUB_ID = "sub_123"
TEST_SOURCE_ID = "ba_123"
TEST_TAX_ID_ID = "txi_123"
TEST_TRANSACTION_ID = "cbtxn_123"


class TestCustomer(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.Customer.list()
        request_mock.assert_requested("get", "/v1/customers")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Customer)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.Customer.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/customers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Customer)

    async def test_is_searchable(self, request_mock):
        resources = await stripe.Customer.search(query='currency:"USD"')
        request_mock.assert_requested(
            "get", "/v1/customers/search", {"query": 'currency:"USD"'}
        )
        assert resources.total_count == 1
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Customer)

        cnt = 0
        async for c in resources.auto_paging_iter():
            assert isinstance(c, stripe.Customer)
            cnt += 1

        assert cnt == 1

    async def test_is_creatable(self, request_mock):
        resource = await stripe.Customer.create()
        request_mock.assert_requested("post", "/v1/customers")
        assert isinstance(resource, stripe.Customer)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.Customer.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        await resource.save()
        request_mock.assert_requested(
            "post", "/v1/customers/%s" % TEST_RESOURCE_ID
        )

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.Customer.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/customers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Customer)

    async def test_is_deletable(self, request_mock):
        resource = await stripe.Customer.retrieve(TEST_RESOURCE_ID)
        await resource.delete()
        request_mock.assert_requested(
            "delete", "/v1/customers/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    async def test_can_delete(self, request_mock):
        resource = await stripe.Customer.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/customers/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    async def test_can_delete_discount(self, request_mock):
        resource = await stripe.Customer.retrieve(TEST_RESOURCE_ID)
        await resource.delete_discount()
        request_mock.assert_requested(
            "delete", "/v1/customers/%s/discount" % TEST_RESOURCE_ID
        )

    async def test_can_delete_discount_class_method(self, request_mock):
        await stripe.Customer.delete_discount(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/customers/%s/discount" % TEST_RESOURCE_ID
        )


class TestCustomerSources(object):
    async def test_is_creatable(self, request_mock):
        await stripe.Customer.create_source(TEST_RESOURCE_ID, source="btok_123")
        request_mock.assert_requested(
            "post", "/v1/customers/%s/sources" % TEST_RESOURCE_ID
        )

    async def test_is_retrievable(self, request_mock):
        await stripe.Customer.retrieve_source(TEST_RESOURCE_ID, TEST_SOURCE_ID)
        request_mock.assert_requested(
            "get",
            "/v1/customers/%s/sources/%s" % (TEST_RESOURCE_ID, TEST_SOURCE_ID),
        )

    async def test_is_modifiable(self, request_mock):
        await stripe.Customer.modify_source(
            TEST_RESOURCE_ID, TEST_SOURCE_ID, metadata={"foo": "bar"}
        )
        request_mock.assert_requested(
            "post",
            "/v1/customers/%s/sources/%s" % (TEST_RESOURCE_ID, TEST_SOURCE_ID),
        )

    async def test_is_deletable(self, request_mock):
        await stripe.Customer.delete_source(TEST_RESOURCE_ID, TEST_SOURCE_ID)
        request_mock.assert_requested(
            "delete",
            "/v1/customers/%s/sources/%s" % (TEST_RESOURCE_ID, TEST_SOURCE_ID),
        )

    async def test_is_listable(self, request_mock):
        resources = await stripe.Customer.list_sources(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/customers/%s/sources" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)


class TestCustomerTaxIds(object):
    async def test_is_creatable(self, request_mock):
        resource = await stripe.Customer.create_tax_id(
            TEST_RESOURCE_ID, type="eu_vat", value="11111"
        )
        request_mock.assert_requested(
            "post", "/v1/customers/%s/tax_ids" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.TaxId)

    async def test_is_retrievable(self, request_mock):
        await stripe.Customer.retrieve_tax_id(TEST_RESOURCE_ID, TEST_TAX_ID_ID)
        request_mock.assert_requested(
            "get",
            "/v1/customers/%s/tax_ids/%s" % (TEST_RESOURCE_ID, TEST_TAX_ID_ID),
        )

    async def test_is_deletable(self, request_mock):
        await stripe.Customer.delete_tax_id(TEST_RESOURCE_ID, TEST_TAX_ID_ID)
        request_mock.assert_requested(
            "delete",
            "/v1/customers/%s/tax_ids/%s" % (TEST_RESOURCE_ID, TEST_TAX_ID_ID),
        )

    async def test_is_listable(self, request_mock):
        resources = await stripe.Customer.list_tax_ids(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/customers/%s/tax_ids" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)


class TestCustomerTransactions(object):
    async def test_is_creatable(self, request_mock):
        resource = await stripe.Customer.create_balance_transaction(
            TEST_RESOURCE_ID, amount=1234, currency="usd"
        )
        request_mock.assert_requested(
            "post", "/v1/customers/%s/balance_transactions" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.CustomerBalanceTransaction)

    async def test_is_retrievable(self, request_mock):
        await stripe.Customer.retrieve_balance_transaction(
            TEST_RESOURCE_ID, TEST_TRANSACTION_ID
        )
        request_mock.assert_requested(
            "get",
            "/v1/customers/%s/balance_transactions/%s"
            % (TEST_RESOURCE_ID, TEST_TRANSACTION_ID),
        )

    async def test_is_listable(self, request_mock):
        resources = await stripe.Customer.list_balance_transactions(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/customers/%s/balance_transactions" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)


class TestCustomerPaymentMethods(object):
    async def test_is_listable(self, request_mock):
        await stripe.Customer.list_payment_methods(TEST_RESOURCE_ID, type="card")
        request_mock.assert_requested(
            "get", "/v1/customers/%s/payment_methods" % TEST_RESOURCE_ID
        )

    async def test_is_listable_on_object(self, request_mock):
        customer = await stripe.Customer.retrieve(
            TEST_RESOURCE_ID
        )
        resource = await customer.list_payment_methods(TEST_RESOURCE_ID, type="card")
        request_mock.assert_requested(
            "get", "/v1/customers/%s/payment_methods" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.ListObject)


class TestCustomerFundingInstructions(object):
    async def test_customer_create_funding_instructions(self, request_mock):
        await stripe.Customer.create_funding_instructions(
            "cus_123",
            bank_transfer={
                "requested_address_types": ["zengin"],
                "type": "jp_bank_transfer",
            },
            currency="usd",
            funding_type="bank_transfer",
        )
        request_mock.assert_requested(
            "post",
            "/v1/customers/cus_123/funding_instructions",
        )


class TestCustomerCashBalanceMethods(object):
    # These tests are present for compatibility purposes. Previously the cash
    # balance methods required None as a second nested_id parameter. The method
    # has been patched to no longer require this, but we want to preserve
    # compatibility for existing users.
    async def test_customer_cashbalance_retrieve_legacy_call_pattern(
        self, request_mock
    ):
        await stripe.Customer.retrieve_cash_balance("cus_123", None)
        request_mock.assert_requested(
            "get", "/v1/customers/cus_123/cash_balance"
        )

    async def test_customer_cashbalance_modify_legacy_call_pattern(
        self, request_mock
    ):
        await stripe.Customer.modify_cash_balance(
            "cus_123",
            None,
            settings={"reconciliation_mode": "manual"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/customers/cus_123/cash_balance",
            {"settings": {"reconciliation_mode": "manual"}},
        )

    async def test_customer_cashbalance_modify_fixed_pattern(self, request_mock):
        await stripe.Customer.modify_cash_balance(
            "cus_123",
            settings={"reconciliation_mode": "manual"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/customers/cus_123/cash_balance",
            {"settings": {"reconciliation_mode": "manual"}},
        )
