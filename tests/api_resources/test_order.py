from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "or_123"


class TestOrder(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.Order.list()
        request_mock.assert_requested("get", "/v1/orders")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Order)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.Order.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/orders/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Order)

    async def test_is_creatable(self, request_mock):
        resource = await stripe.Order.create(currency="usd")
        request_mock.assert_requested("post", "/v1/orders")
        assert isinstance(resource, stripe.Order)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.Order.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        await resource.save()
        request_mock.assert_requested(
            "post", "/v1/orders/%s" % TEST_RESOURCE_ID
        )

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.Order.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/orders/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Order)

    async def test_can_pay(self, request_mock):
        order = await stripe.Order.retrieve(TEST_RESOURCE_ID)
        resource = await order.pay(source="src_123")
        request_mock.assert_requested(
            "post",
            "/v1/orders/%s/pay" % TEST_RESOURCE_ID,
            {"source": "src_123"},
        )
        assert isinstance(resource, stripe.Order)
        assert resource is order

    async def test_can_pay_classmethod(self, request_mock):
        resource = await stripe.Order.pay(TEST_RESOURCE_ID, source="src_123")
        request_mock.assert_requested(
            "post",
            "/v1/orders/%s/pay" % TEST_RESOURCE_ID,
            {"source": "src_123"},
        )
        assert isinstance(resource, stripe.Order)

    async def test_can_return(self, request_mock):
        order = await stripe.Order.retrieve(TEST_RESOURCE_ID)
        resource = await order.return_order()
        request_mock.assert_requested(
            "post", "/v1/orders/%s/returns" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.OrderReturn)

    async def test_can_return_classmethod(self, request_mock):
        resource = await stripe.Order.return_order(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/orders/%s/returns" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.OrderReturn)
