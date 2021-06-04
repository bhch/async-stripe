from __future__ import absolute_import, division, print_function

import pytest

import stripe


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "txi_123"


class TestTaxId(object):
    def construct_resource(self):
        tax_id_dict = {
            "id": TEST_RESOURCE_ID,
            "object": "tax_id",
            "customer": "cus_123",
        }
        return stripe.TaxId.construct_from(tax_id_dict, stripe.api_key)

    async def test_has_instance_url(self, request_mock):
        resource = self.construct_resource()
        assert (
            resource.instance_url()
            == "/v1/customers/cus_123/tax_ids/%s" % TEST_RESOURCE_ID
        )

    async def test_is_not_retrievable(self, request_mock):
        with pytest.raises(NotImplementedError):
            await stripe.TaxId.retrieve(TEST_RESOURCE_ID)
