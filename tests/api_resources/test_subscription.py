from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "sub_123"


class TestSubscription(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.Subscription.list()
        request_mock.assert_requested("get", "/v1/subscriptions")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Subscription)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.Subscription.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/subscriptions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Subscription)

    async def test_is_searchable(self, request_mock):
        resources = await stripe.Subscription.search(query='currency:"USD"')
        request_mock.assert_requested(
            "get", "/v1/subscriptions/search", {"query": 'currency:"USD"'}
        )
        assert resources.total_count == 1
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Subscription)

        cnt = 0
        async for c in resources.auto_paging_iter():
            assert isinstance(c, stripe.Subscription)
            cnt += 1

        assert cnt == 1

    async def test_is_creatable(self, request_mock):
        resource = await stripe.Subscription.create(customer="cus_123")
        request_mock.assert_requested("post", "/v1/subscriptions")
        assert isinstance(resource, stripe.Subscription)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.Subscription.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        await resource.save()
        request_mock.assert_requested(
            "post", "/v1/subscriptions/%s" % TEST_RESOURCE_ID
        )

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.Subscription.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/subscriptions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Subscription)

    async def test_is_deletable(self, request_mock):
        resource = await stripe.Subscription.retrieve(TEST_RESOURCE_ID)
        await resource.delete()
        request_mock.assert_requested(
            "delete", "/v1/subscriptions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Subscription)

    async def test_can_delete(self, request_mock):
        resource = await stripe.Subscription.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/subscriptions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Subscription)

    async def test_can_delete_discount(self, request_mock):
        sub = await stripe.Subscription.retrieve(TEST_RESOURCE_ID)
        await sub.delete_discount()
        request_mock.assert_requested(
            "delete", "/v1/subscriptions/%s/discount" % sub.id
        )

    async def test_can_delete_discount_classmethod(self, request_mock):
        await stripe.Subscription.delete_discount(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/subscriptions/%s/discount" % TEST_RESOURCE_ID
        )
