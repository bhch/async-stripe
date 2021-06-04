from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "tu_123"


class TestTopup(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.Topup.list()
        request_mock.assert_requested("get", "/v1/topups")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Topup)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.Topup.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/topups/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Topup)

    async def test_is_creatable(self, request_mock):
        resource = await stripe.Topup.create(
            amount=100,
            currency="usd",
            source="src_123",
            description="description",
            statement_descriptor="statement descriptor",
        )
        request_mock.assert_requested("post", "/v1/topups")
        assert isinstance(resource, stripe.Topup)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.Topup.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        await resource.save()
        request_mock.assert_requested(
            "post", "/v1/topups/%s" % TEST_RESOURCE_ID
        )

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.Topup.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/topups/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Topup)

    async def test_can_cancel(self, request_mock):
        resource = await stripe.Topup.retrieve(TEST_RESOURCE_ID)
        resource = await resource.cancel()
        request_mock.assert_requested(
            "post", "/v1/topups/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Topup)

    async def test_can_cancel_classmethod(self, request_mock):
        resource = await stripe.Topup.cancel(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/topups/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Topup)
