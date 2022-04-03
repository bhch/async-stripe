from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "ch_123"


class TestCharge(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.Charge.list()
        request_mock.assert_requested("get", "/v1/charges")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Charge)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.Charge.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/charges/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Charge)

    async def test_is_searchable(self, request_mock):
        resources = await stripe.Charge.search(query='currency:"USD"')
        request_mock.assert_requested(
            "get", "/v1/charges/search", {"query": 'currency:"USD"'}
        )
        assert resources.total_count == 1
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Charge)

        cnt = 0
        async for c in resources.auto_paging_iter():
            assert isinstance(c, stripe.Charge)
            cnt += 1

        assert cnt == 1

    async def test_is_creatable(self, request_mock):
        resource = await stripe.Charge.create(
            amount=100, currency="usd", source="tok_123"
        )
        request_mock.assert_requested("post", "/v1/charges")
        assert isinstance(resource, stripe.Charge)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.Charge.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        await resource.save()
        request_mock.assert_requested(
            "post", "/v1/charges/%s" % TEST_RESOURCE_ID
        )

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.Charge.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/charges/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Charge)

    async def test_is_refundable(self, request_mock):
        charge = await stripe.Charge.retrieve(TEST_RESOURCE_ID)
        resource = await charge.refund()
        request_mock.assert_requested(
            "post", "/v1/charges/%s/refund" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Charge)

    async def test_can_capture(self, request_mock):
        charge = await stripe.Charge.retrieve(TEST_RESOURCE_ID)
        resource = await charge.capture()
        request_mock.assert_requested(
            "post", "/v1/charges/%s/capture" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Charge)

    async def test_can_capture_classmethod(self, request_mock):
        resource = await stripe.Charge.capture(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/charges/%s/capture" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Charge)

    async def test_can_update_dispute(self, request_mock):
        charge = await stripe.Charge.retrieve(TEST_RESOURCE_ID)
        resource = await charge.update_dispute()
        request_mock.assert_requested(
            "post", "/v1/charges/%s/dispute" % charge.id
        )
        assert isinstance(resource, stripe.Dispute)

    async def test_can_close_dispute(self, request_mock):
        charge = await stripe.Charge.retrieve(TEST_RESOURCE_ID)
        resource = await charge.close_dispute()
        request_mock.assert_requested(
            "post", "/v1/charges/%s/dispute/close" % charge.id
        )
        assert isinstance(resource, stripe.Dispute)

    async def test_can_mark_as_fraudulent(self, request_mock):
        charge = await stripe.Charge.retrieve(TEST_RESOURCE_ID)
        resource = await charge.mark_as_fraudulent()
        request_mock.assert_requested(
            "post",
            "/v1/charges/%s" % charge.id,
            {"fraud_details": {"user_report": "fraudulent"}},
        )
        assert isinstance(resource, stripe.Charge)

    async def test_can_mark_as_safe(self, request_mock):
        charge = await stripe.Charge.retrieve(TEST_RESOURCE_ID)
        resource = await charge.mark_as_safe()
        request_mock.assert_requested(
            "post",
            "/v1/charges/%s" % charge.id,
            {"fraud_details": {"user_report": "safe"}},
        )
        assert isinstance(resource, stripe.Charge)
