from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "vs_123"


class TestVerificationReport(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.identity.VerificationReport.list()
        request_mock.assert_requested(
            "get", "/v1/identity/verification_reports"
        )
        assert isinstance(resources.data, list)
        assert isinstance(
            resources.data[0], stripe.identity.VerificationReport
        )

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.identity.VerificationReport.retrieve(
            TEST_RESOURCE_ID
        )
        request_mock.assert_requested(
            "get", "/v1/identity/verification_reports/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.identity.VerificationReport)
