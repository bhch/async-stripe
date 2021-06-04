from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio


TEST_RESOURCE_ID = "price_123"


class TestPrice(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.Price.list()
        request_mock.assert_requested("get", "/v1/prices")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Price)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.Price.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/prices/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Price)

    async def test_is_creatable(self, request_mock):
        resource = await stripe.Price.create(
            unit_amount=1000,
            currency="usd",
            recurring={"interval": "month"},
            product_data={"name": "price_nickname"},
        )
        request_mock.assert_requested("post", "/v1/prices")
        assert isinstance(resource, stripe.Price)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.Price.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        await resource.save()
        request_mock.assert_requested(
            "post", "/v1/prices/%s" % TEST_RESOURCE_ID
        )

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.Price.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/prices/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Price)
