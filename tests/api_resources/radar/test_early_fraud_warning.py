from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "issfr_123"


class TestEarlyFraudWarning(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.radar.EarlyFraudWarning.list()
        request_mock.assert_requested("get", "/v1/radar/early_fraud_warnings")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.radar.EarlyFraudWarning)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.radar.EarlyFraudWarning.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/radar/early_fraud_warnings/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.radar.EarlyFraudWarning)
