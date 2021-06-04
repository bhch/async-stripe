from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio


TEST_RESOURCE_ID = "link_123"


class TestFileLink(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.FileLink.list()
        request_mock.assert_requested("get", "/v1/file_links")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.FileLink)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.FileLink.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/file_links/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.FileLink)

    async def test_is_creatable(self, request_mock):
        resource = await stripe.FileLink.create(file="file_123")
        request_mock.assert_requested("post", "/v1/file_links")
        assert isinstance(resource, stripe.FileLink)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.FileLink.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        await resource.save()
        request_mock.assert_requested(
            "post", "/v1/file_links/%s" % TEST_RESOURCE_ID
        )

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.FileLink.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/file_links/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.FileLink)
