from __future__ import absolute_import, division, print_function

import stripe

import pytest

pytestmark = pytest.mark.asyncio


TEST_RESOURCE_ID = "cs_123"


class TestSession(object):
    async def test_is_creatable(self, request_mock):
        resource = await stripe.checkout.Session.create(
            cancel_url="https://stripe.com/cancel",
            client_reference_id="1234",
            line_items=[
                {
                    "amount": 123,
                    "currency": "usd",
                    "description": "item 1",
                    "images": ["https://stripe.com/img1"],
                    "name": "name",
                    "quantity": 2,
                }
            ],
            payment_intent_data={"receipt_email": "test@stripe.com"},
            payment_method_types=["card"],
            success_url="https://stripe.com/success",
        )
        request_mock.assert_requested("post", "/v1/checkout/sessions")
        assert isinstance(resource, stripe.checkout.Session)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.checkout.Session.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/checkout/sessions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.checkout.Session)

    async def test_checkout_session_expire(self, request_mock):
        await stripe.checkout.Session.expire(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post",
            "/v1/checkout/sessions/%s/expire" % TEST_RESOURCE_ID,
        )


class TestSessionLineItems(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.checkout.Session.list_line_items(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/checkout/sessions/%s/line_items" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.LineItem)
