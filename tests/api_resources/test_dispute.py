from __future__ import absolute_import, division, print_function

import stripe

import pytest

pytestmark = pytest.mark.asyncio


TEST_RESOURCE_ID = "dp_123"


class TestDispute(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.Dispute.list()
        request_mock.assert_requested("get", "/v1/disputes")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Dispute)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.Dispute.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/disputes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Dispute)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.Dispute.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        await resource.save()
        request_mock.assert_requested(
            "post", "/v1/disputes/%s" % TEST_RESOURCE_ID
        )

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.Dispute.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/disputes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Dispute)

    async def test_can_close(self, request_mock):
        resource = await stripe.Dispute.retrieve(TEST_RESOURCE_ID)
        await resource.close()
        request_mock.assert_requested(
            "post", "/v1/disputes/%s/close" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Dispute)

    async def test_can_close_classmethod(self, request_mock):
        resource = await stripe.Dispute.close(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/disputes/%s/close" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Dispute)
