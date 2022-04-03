from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "prod_123"


class TestProduct(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.Product.list()
        request_mock.assert_requested("get", "/v1/products")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Product)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.Product.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/products/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Product)

    async def test_is_searchable(self, request_mock):
        resources = await stripe.Product.search(query='currency:"USD"')
        request_mock.assert_requested(
            "get", "/v1/products/search", {"query": 'currency:"USD"'}
        )
        assert resources.total_count == 1
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Product)

        cnt = 0
        async for c in resources.auto_paging_iter():
            assert isinstance(c, stripe.Product)
            cnt += 1

        assert cnt == 1

    async def test_is_creatable(self, request_mock):
        resource = await stripe.Product.create(name="NAME")
        request_mock.assert_requested("post", "/v1/products")
        assert isinstance(resource, stripe.Product)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.Product.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        await resource.save()
        request_mock.assert_requested(
            "post", "/v1/products/%s" % TEST_RESOURCE_ID
        )

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.Product.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/products/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Product)

    async def test_is_deletable(self, request_mock):
        resource = await stripe.Product.retrieve(TEST_RESOURCE_ID)
        await resource.delete()
        request_mock.assert_requested(
            "delete", "/v1/products/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    async def test_can_delete(self, request_mock):
        resource = await stripe.Product.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/products/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
