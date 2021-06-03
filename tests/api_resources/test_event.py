from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio


TEST_RESOURCE_ID = "evt_123"


class TestEvent(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.Event.list()
        request_mock.assert_requested("get", "/v1/events")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Event)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.Event.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/events/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Event)
