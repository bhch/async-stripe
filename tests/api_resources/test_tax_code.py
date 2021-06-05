from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "txcd_123"


class TestTaxCode(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.TaxCode.list()
        request_mock.assert_requested("get", "/v1/tax_codes")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.TaxCode)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.TaxCode.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/tax_codes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.TaxCode)
