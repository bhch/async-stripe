from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio


TEST_RESOURCE_ID = "txr_123"


class TestTaxRate(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.TaxRate.list()
        request_mock.assert_requested("get", "/v1/tax_rates")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.TaxRate)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.TaxRate.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/tax_rates/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.TaxRate)

    async def test_is_creatable(self, request_mock):
        resource = await stripe.TaxRate.create(
            display_name="name", inclusive=False, percentage=10.15
        )
        request_mock.assert_requested("post", "/v1/tax_rates")
        assert isinstance(resource, stripe.TaxRate)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.TaxRate.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        await resource.save()
        request_mock.assert_requested(
            "post", "/v1/tax_rates/%s" % TEST_RESOURCE_ID
        )

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.TaxRate.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/tax_rates/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.TaxRate)
