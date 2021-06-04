from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "seti_123"


class TestSetupIntent(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.SetupIntent.list()
        request_mock.assert_requested("get", "/v1/setup_intents")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.SetupIntent)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.SetupIntent.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/setup_intents/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.SetupIntent)

    async def test_is_creatable(self, request_mock):
        resource = await stripe.SetupIntent.create(payment_method_types=["card"])
        request_mock.assert_requested("post", "/v1/setup_intents")
        assert isinstance(resource, stripe.SetupIntent)

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.SetupIntent.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post",
            "/v1/setup_intents/%s" % TEST_RESOURCE_ID,
            {"metadata": {"key": "value"}},
        )
        assert isinstance(resource, stripe.SetupIntent)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.SetupIntent.retrieve(TEST_RESOURCE_ID)

        resource.metadata["key"] = "value"
        await resource.save()
        request_mock.assert_requested(
            "post",
            "/v1/setup_intents/%s" % TEST_RESOURCE_ID,
            {"metadata": {"key": "value"}},
        )
        assert isinstance(resource, stripe.SetupIntent)

    async def test_can_cancel(self, request_mock):
        resource = await stripe.SetupIntent.retrieve(TEST_RESOURCE_ID)
        await resource.cancel()
        request_mock.assert_requested(
            "post", "/v1/setup_intents/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.SetupIntent)

    async def test_can_cancel_classmethod(self, request_mock):
        resource = await stripe.SetupIntent.cancel(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/setup_intents/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.SetupIntent)

    async def test_can_confirm(self, request_mock):
        resource = await stripe.SetupIntent.retrieve(TEST_RESOURCE_ID)
        await resource.confirm()
        request_mock.assert_requested(
            "post", "/v1/setup_intents/%s/confirm" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.SetupIntent)

    async def test_can_confirm_classmethod(self, request_mock):
        resource = await stripe.SetupIntent.confirm(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/setup_intents/%s/confirm" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.SetupIntent)
