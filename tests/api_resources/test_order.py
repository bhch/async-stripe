from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "or_123"


class TestOrder(object):
    async def test_order_create(self, request_mock):
        await stripe.Order.create(
            description="description",
            currency="usd",
            line_items=[{"description": "my line item"}],
        )
        request_mock.assert_requested("post", "/v1/orders")

    async def test_order_update(self, request_mock):
        await stripe.Order.modify("order_xyz")
        request_mock.assert_requested("post", "/v1/orders/order_xyz")

    async def test_order_list_line_items(self, request_mock):
        await stripe.Order.list_line_items("order_xyz")
        request_mock.assert_requested("get", "/v1/orders/order_xyz/line_items")

    async def test_order_cancel(self, request_mock):
        await stripe.Order.cancel("order_xyz")
        request_mock.assert_requested("post", "/v1/orders/order_xyz/cancel")

    async def test_order_reopen(self, request_mock):
        await stripe.Order.reopen("order_xyz")
        request_mock.assert_requested("post", "/v1/orders/order_xyz/reopen")

    async def test_order_submit(self, request_mock):
        await stripe.Order.submit("order_xyz", expected_total=100)
        request_mock.assert_requested("post", "/v1/orders/order_xyz/submit")

    async def test_order_update2(self, request_mock):
        await stripe.Order.modify("order_xyz")
        request_mock.assert_requested("post", "/v1/orders/order_xyz")
