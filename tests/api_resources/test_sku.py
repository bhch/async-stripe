from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "sku_123"


class TestSKU(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.SKU.list()
        request_mock.assert_requested("get", "/v1/skus")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.SKU)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.SKU.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v1/skus/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, stripe.SKU)

    async def test_is_creatable(self, request_mock):
        resource = await stripe.SKU.create(
            currency="usd",
            inventory=dict(type="finite", quantity=500),
            price=100,
            product="prod_123",
        )
        request_mock.assert_requested("post", "/v1/skus")
        assert isinstance(resource, stripe.SKU)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.SKU.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        await resource.save()
        request_mock.assert_requested("post", "/v1/skus/%s" % TEST_RESOURCE_ID)

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.SKU.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested("post", "/v1/skus/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, stripe.SKU)

    async def test_is_deletable(self, request_mock):
        resource = await stripe.SKU.retrieve(TEST_RESOURCE_ID)
        await resource.delete()
        request_mock.assert_requested(
            "delete", "/v1/skus/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    async def test_can_delete(self, request_mock):
        resource = await stripe.SKU.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/skus/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
