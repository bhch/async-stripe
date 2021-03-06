from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "si_123"


class TestSubscriptionItem(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.SubscriptionItem.list(subscription="sub_123")
        request_mock.assert_requested(
            "get", "/v1/subscription_items", {"subscription": "sub_123"}
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.SubscriptionItem)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.SubscriptionItem.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/subscription_items/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.SubscriptionItem)

    async def test_is_creatable(self, request_mock):
        resource = await stripe.SubscriptionItem.create(
            price="price_123", subscription="sub_123"
        )
        request_mock.assert_requested("post", "/v1/subscription_items")
        assert isinstance(resource, stripe.SubscriptionItem)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.SubscriptionItem.retrieve(TEST_RESOURCE_ID)
        resource.price = "price_123"
        await resource.save()
        request_mock.assert_requested(
            "post",
            "/v1/subscription_items/%s" % TEST_RESOURCE_ID,
            {"price": "price_123"},
        )

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.SubscriptionItem.modify(
            TEST_RESOURCE_ID, price="price_123"
        )
        request_mock.assert_requested(
            "post",
            "/v1/subscription_items/%s" % TEST_RESOURCE_ID,
            {"price": "price_123"},
        )
        assert isinstance(resource, stripe.SubscriptionItem)

    async def test_is_deletable(self, request_mock):
        resource = await stripe.SubscriptionItem.retrieve(TEST_RESOURCE_ID)
        await resource.delete()
        request_mock.assert_requested(
            "delete", "/v1/subscription_items/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    async def test_can_delete(self, request_mock):
        resource = await stripe.SubscriptionItem.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/subscription_items/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True


class TestUsageRecords(object):
    async def test_is_creatable(self, request_mock):
        resource = await stripe.SubscriptionItem.create_usage_record(
            TEST_RESOURCE_ID,
            quantity=5000,
            timestamp=1524182400,
            action="increment",
        )
        request_mock.assert_requested(
            "post",
            "/v1/subscription_items/%s/usage_records" % TEST_RESOURCE_ID,
        )
        assert isinstance(resource, stripe.UsageRecord)


class TestUsageRecordSummaries(object):
    async def test_is_listable(self, request_mock):
        resource = await stripe.SubscriptionItem.list_usage_record_summaries(
            TEST_RESOURCE_ID
        )
        request_mock.assert_requested(
            "get",
            "/v1/subscription_items/%s/usage_record_summaries"
            % TEST_RESOURCE_ID,
        )
        assert isinstance(resource.data, list)
        assert isinstance(resource.data[0], stripe.UsageRecordSummary)
