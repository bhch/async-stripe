from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "pi_123"


class TestPaymentIntent(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.PaymentIntent.list()
        request_mock.assert_requested("get", "/v1/payment_intents")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.PaymentIntent)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.PaymentIntent.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/payment_intents/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)

    async def test_is_searchable(self, request_mock):
        resources = await stripe.PaymentIntent.search(query='currency:"USD"')
        request_mock.assert_requested(
            "get", "/v1/payment_intents/search", {"query": 'currency:"USD"'}
        )
        assert resources.total_count == 1
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.PaymentIntent)

        cnt = 0
        async for c in resources.auto_paging_iter():
            assert isinstance(c, stripe.PaymentIntent)
            cnt += 1

        assert cnt == 1

    async def test_is_creatable(self, request_mock):
        resource = await stripe.PaymentIntent.create(
            amount="1234", currency="amount", payment_method_types=["card"]
        )
        request_mock.assert_requested("post", "/v1/payment_intents")
        assert isinstance(resource, stripe.PaymentIntent)

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.PaymentIntent.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents/%s" % TEST_RESOURCE_ID,
            {"metadata": {"key": "value"}},
        )
        assert isinstance(resource, stripe.PaymentIntent)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.PaymentIntent.retrieve(TEST_RESOURCE_ID)

        resource.metadata["key"] = "value"
        await resource.save()
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents/%s" % TEST_RESOURCE_ID,
            {"metadata": {"key": "value"}},
        )
        assert isinstance(resource, stripe.PaymentIntent)

    async def test_can_cancel(self, request_mock):
        resource = await stripe.PaymentIntent.retrieve(TEST_RESOURCE_ID)
        await resource.cancel()
        request_mock.assert_requested(
            "post", "/v1/payment_intents/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)

    async def test_can_cancel_classmethod(self, request_mock):
        resource = await stripe.PaymentIntent.cancel(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/payment_intents/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)

    async def test_can_capture(self, request_mock):
        resource = await stripe.PaymentIntent.retrieve(TEST_RESOURCE_ID)
        await resource.capture()
        request_mock.assert_requested(
            "post", "/v1/payment_intents/%s/capture" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)

    async def test_can_capture_classmethod(self, request_mock):
        resource = await stripe.PaymentIntent.capture(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/payment_intents/%s/capture" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)

    async def test_can_confirm(self, request_mock):
        resource = await stripe.PaymentIntent.retrieve(TEST_RESOURCE_ID)
        await resource.confirm()
        request_mock.assert_requested(
            "post", "/v1/payment_intents/%s/confirm" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)

    async def test_can_confirm_classmethod(self, request_mock):
        resource = await stripe.PaymentIntent.confirm(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/payment_intents/%s/confirm" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)

    async def test_paymentintent_verify_microdeposits(self, request_mock):
        await stripe.PaymentIntent.verify_microdeposits("pi_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents/pi_xxxxxxxxxxxxx/verify_microdeposits",
        )
