from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio


TEST_RESOURCE_ID = "tdsrc_123"


class TestThreeDSecure(object):
    async def test_is_retrievable(self, request_mock):
        resource = await stripe.ThreeDSecure.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/3d_secure/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.ThreeDSecure)

    async def test_is_creatable(self, request_mock):
        resource = await stripe.ThreeDSecure.create(
            card="tok_123", amount=100, currency="usd", return_url="url"
        )
        request_mock.assert_requested("post", "/v1/3d_secure")
        assert isinstance(resource, stripe.ThreeDSecure)
