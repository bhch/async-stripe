from __future__ import absolute_import, division, print_function

import stripe

import pytest

pytestmark = pytest.mark.asyncio


TEST_RESOURCE_ID = "shr_123"


class TestShippingRate(object):
    async def test_shippingrate_create(self, request_mock):
        await stripe.ShippingRate.create(
            display_name="Sample Shipper",
            fixed_amount={"currency": "usd", "amount": 400},
            type="fixed_amount",
        )
        request_mock.assert_requested("post", "/v1/shipping_rates")

    async def test_shippingrate_list(self, request_mock):
        await stripe.ShippingRate.list()
        request_mock.assert_requested("get", "/v1/shipping_rates")

    async def test_checkout_session_create2(self, request_mock):
        await stripe.checkout.Session.create(
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
            mode="payment",
            shipping_options=[
                {"shipping_rate": TEST_RESOURCE_ID},
                {
                    "shipping_rate_data": {
                        "display_name": "Standard",
                        "delivery_estimate": {
                            "minimum": {"unit": "day", "value": 5},
                            "maximum": {"unit": "day", "value": 7},
                        },
                    },
                },
            ],
        )
        request_mock.assert_requested("post", "/v1/checkout/sessions")