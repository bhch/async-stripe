from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "pl_xyz"


class TestPaymentLink(object):
    async def test_paymentlink_create(self, request_mock):
        await stripe.PaymentLink.create(
            line_items=[{"price": "price_xxxxxxxxxxxxx", "quantity": 1}],
        )
        request_mock.assert_requested("post", "/v1/payment_links")

    async def test_paymentlink_list_line_items(self, request_mock):
        await stripe.PaymentLink.list_line_items(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/payment_links/%s/line_items" % TEST_RESOURCE_ID
        )

    async def test_paymentlink_retrieve(self, request_mock):
        await stripe.PaymentLink.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v1/payment_links/%s" % TEST_RESOURCE_ID)
