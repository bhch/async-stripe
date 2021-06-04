from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio


TEST_RESOURCE_ID = "usd"


class TestExchangeRate(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.ExchangeRate.list()
        request_mock.assert_requested("get", "/v1/exchange_rates")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.ExchangeRate)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.ExchangeRate.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/exchange_rates/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.ExchangeRate)
