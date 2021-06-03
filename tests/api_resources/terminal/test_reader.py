from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "rdr_123"


class TestReader(object):
    async def test_is_creatable(self, request_mock):
        resource = await stripe.terminal.Reader.create(
            registration_code="a-b-c", label="name"
        )
        request_mock.assert_requested("post", "/v1/terminal/readers")
        assert isinstance(resource, stripe.terminal.Reader)

    async def test_is_listable(self, request_mock):
        resources = await stripe.terminal.Reader.list()
        request_mock.assert_requested("get", "/v1/terminal/readers")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.terminal.Reader)

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.terminal.Reader.modify(
            TEST_RESOURCE_ID, label="new-name"
        )
        request_mock.assert_requested(
            "post", "/v1/terminal/readers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.terminal.Reader)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.terminal.Reader.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/terminal/readers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.terminal.Reader)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.terminal.Reader.retrieve(TEST_RESOURCE_ID)
        resource.label = "new-name"
        reader = await resource.save()
        request_mock.assert_requested(
            "post", "/v1/terminal/readers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.terminal.Reader)
        assert resource is reader

    async def test_is_deletable(self, request_mock):
        resource = await stripe.terminal.Reader.retrieve(TEST_RESOURCE_ID)
        await resource.delete()
        request_mock.assert_requested(
            "delete", "/v1/terminal/readers/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    async def test_can_delete(self, request_mock):
        resource = await stripe.terminal.Reader.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/terminal/readers/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
