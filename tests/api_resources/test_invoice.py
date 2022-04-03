from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "in_123"


class TestInvoice(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.Invoice.list()
        request_mock.assert_requested("get", "/v1/invoices")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Invoice)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/invoices/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    async def test_is_searchable(self, request_mock):
        resources = await stripe.Invoice.search(query='currency:"USD"')
        request_mock.assert_requested(
            "get", "/v1/invoices/search", {"query": 'currency:"USD"'}
        )
        assert resources.total_count == 1
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Invoice)

        cnt = 0
        async for c in resources.auto_paging_iter():
            assert isinstance(c, stripe.Invoice)
            cnt += 1

        assert cnt == 1

    async def test_is_creatable(self, request_mock):
        resource = await stripe.Invoice.create(customer="cus_123")
        request_mock.assert_requested("post", "/v1/invoices")
        assert isinstance(resource, stripe.Invoice)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        await resource.save()
        request_mock.assert_requested(
            "post", "/v1/invoices/%s" % TEST_RESOURCE_ID
        )

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.Invoice.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/invoices/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    async def test_is_deletable(self, request_mock):
        resource = await stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        await resource.delete()
        request_mock.assert_requested(
            "delete", "/v1/invoices/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    async def test_can_delete(self, request_mock):
        resource = await stripe.Invoice.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/invoices/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    async def test_can_finalize_invoice(self, request_mock):
        resource = await stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        resource = await resource.finalize_invoice()
        request_mock.assert_requested(
            "post", "/v1/invoices/%s/finalize" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    async def test_can_finalize_invoice_classmethod(self, request_mock):
        resource = await stripe.Invoice.finalize_invoice(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/invoices/%s/finalize" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    async def test_can_mark_uncollectible(self, request_mock):
        resource = await stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        resource = await resource.mark_uncollectible()
        request_mock.assert_requested(
            "post", "/v1/invoices/%s/mark_uncollectible" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    async def test_can_mark_uncollectible_classmethod(self, request_mock):
        resource = await stripe.Invoice.mark_uncollectible(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/invoices/%s/mark_uncollectible" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    async def test_can_pay(self, request_mock):
        resource = await stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        resource = await resource.pay()
        request_mock.assert_requested(
            "post", "/v1/invoices/%s/pay" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    async def test_can_pay_classmethod(self, request_mock):
        resource = await stripe.Invoice.pay(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/invoices/%s/pay" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    async def test_can_send_invoice(self, request_mock):
        resource = await stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        resource = await resource.send_invoice()
        request_mock.assert_requested(
            "post", "/v1/invoices/%s/send" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    async def test_can_send_invoice_classmethod(self, request_mock):
        resource = await stripe.Invoice.send_invoice(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/invoices/%s/send" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    async def test_can_upcoming(self, request_mock):
        resource = await stripe.Invoice.upcoming(customer="cus_123")
        request_mock.assert_requested("get", "/v1/invoices/upcoming")
        assert isinstance(resource, stripe.Invoice)

    async def test_can_void_invoice(self, request_mock):
        resource = await stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        resource = await resource.void_invoice()
        request_mock.assert_requested(
            "post", "/v1/invoices/%s/void" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    async def test_can_void_invoice_classmethod(self, request_mock):
        resource = await stripe.Invoice.void_invoice(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/invoices/%s/void" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)
