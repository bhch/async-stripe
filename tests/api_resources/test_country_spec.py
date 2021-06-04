from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio


TEST_RESOURCE_ID = "US"


class TestCountrySpec(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.CountrySpec.list()
        request_mock.assert_requested("get", "/v1/country_specs")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.CountrySpec)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.CountrySpec.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/country_specs/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.CountrySpec)
