from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "rsli_123"


class TestValueListItem(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.radar.ValueListItem.list(value_list="rsl_123")
        request_mock.assert_requested("get", "/v1/radar/value_list_items")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.radar.ValueListItem)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.radar.ValueListItem.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/radar/value_list_items/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.radar.ValueListItem)

    async def test_is_creatable(self, request_mock):
        resource = await stripe.radar.ValueListItem.create(
            value_list="rsl_123", value="value"
        )
        request_mock.assert_requested("post", "/v1/radar/value_list_items")
        assert isinstance(resource, stripe.radar.ValueListItem)

    async def test_is_deletable(self, request_mock):
        resource = await stripe.radar.ValueListItem.retrieve(TEST_RESOURCE_ID)
        await resource.delete()
        request_mock.assert_requested(
            "delete", "/v1/radar/value_list_items/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    async def test_can_delete(self, request_mock):
        resource = await stripe.radar.ValueListItem.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/radar/value_list_items/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
