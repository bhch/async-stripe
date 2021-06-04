from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "rp_123"


class TestRecipient(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.Recipient.list()
        request_mock.assert_requested("get", "/v1/recipients")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Recipient)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.Recipient.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/recipients/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Recipient)

    async def test_is_creatable(self, request_mock):
        resource = await stripe.Recipient.create(type="individual", name="NAME")
        request_mock.assert_requested("post", "/v1/recipients")
        assert isinstance(resource, stripe.Recipient)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.Recipient.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        await resource.save()
        request_mock.assert_requested(
            "post", "/v1/recipients/%s" % TEST_RESOURCE_ID
        )

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.Recipient.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/recipients/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Recipient)

    async def test_is_deletable(self, request_mock):
        resource = await stripe.Recipient.retrieve(TEST_RESOURCE_ID)
        await resource.delete()
        request_mock.assert_requested(
            "delete", "/v1/recipients/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    async def test_can_delete(self, request_mock):
        resource = await stripe.Recipient.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/recipients/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
