from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio


TEST_RESOURCE_ID = "sub_sched_123"


class TestSubscriptionScheduleSchedule(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.SubscriptionSchedule.list()
        request_mock.assert_requested("get", "/v1/subscription_schedules")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.SubscriptionSchedule)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.SubscriptionSchedule.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/subscription_schedules/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.SubscriptionSchedule)

    async def test_is_creatable(self, request_mock):
        resource = await stripe.SubscriptionSchedule.create(customer="cus_123")
        request_mock.assert_requested("post", "/v1/subscription_schedules")
        assert isinstance(resource, stripe.SubscriptionSchedule)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.SubscriptionSchedule.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        await resource.save()
        request_mock.assert_requested(
            "post", "/v1/subscription_schedules/%s" % TEST_RESOURCE_ID
        )

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.SubscriptionSchedule.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/subscription_schedules/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.SubscriptionSchedule)

    async def test_can_cancel(self, request_mock):
        resource = await stripe.SubscriptionSchedule.retrieve(TEST_RESOURCE_ID)
        resource = await resource.cancel()
        request_mock.assert_requested(
            "post", "/v1/subscription_schedules/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.SubscriptionSchedule)

    async def test_can_cancel_classmethod(self, request_mock):
        resource = await stripe.SubscriptionSchedule.cancel(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/subscription_schedules/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.SubscriptionSchedule)

    async def test_can_release(self, request_mock):
        resource = await stripe.SubscriptionSchedule.retrieve(TEST_RESOURCE_ID)
        resource = await resource.release()
        request_mock.assert_requested(
            "post", "/v1/subscription_schedules/%s/release" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.SubscriptionSchedule)

    async def test_can_release_classmethod(self, request_mock):
        resource = await stripe.SubscriptionSchedule.release(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/subscription_schedules/%s/release" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.SubscriptionSchedule)
