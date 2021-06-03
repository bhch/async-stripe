from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "we_123"


class TestWebhookEndpoint(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.WebhookEndpoint.list()
        request_mock.assert_requested("get", "/v1/webhook_endpoints")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.WebhookEndpoint)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.WebhookEndpoint.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/webhook_endpoints/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.WebhookEndpoint)

    async def test_is_creatable(self, request_mock):
        resource = await stripe.WebhookEndpoint.create(
            enabled_events=["charge.succeeded"], url="https://stripe.com"
        )
        request_mock.assert_requested("post", "/v1/webhook_endpoints")
        assert isinstance(resource, stripe.WebhookEndpoint)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.WebhookEndpoint.retrieve(TEST_RESOURCE_ID)
        resource.enabled_events = ["charge.succeeded"]
        await resource.save()
        request_mock.assert_requested(
            "post", "/v1/webhook_endpoints/%s" % TEST_RESOURCE_ID
        )

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.WebhookEndpoint.modify(
            TEST_RESOURCE_ID,
            enabled_events=["charge.succeeded"],
            url="https://stripe.com",
        )
        request_mock.assert_requested(
            "post", "/v1/webhook_endpoints/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.WebhookEndpoint)

    async def test_is_deletable(self, request_mock):
        resource = await stripe.WebhookEndpoint.retrieve(TEST_RESOURCE_ID)
        await resource.delete()
        request_mock.assert_requested(
            "delete", "/v1/webhook_endpoints/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    async def test_can_delete(self, request_mock):
        resource = await stripe.WebhookEndpoint.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/webhook_endpoints/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
