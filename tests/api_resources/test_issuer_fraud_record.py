from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio


TEST_RESOURCE_ID = "issfr_123"


class TestIssuerFraudRecord(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.IssuerFraudRecord.list()
        request_mock.assert_requested("get", "/v1/issuer_fraud_records")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.IssuerFraudRecord)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.IssuerFraudRecord.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/issuer_fraud_records/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.IssuerFraudRecord)
