from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio


TEST_RESOURCE_ID = 'rf_123'


class TestRefund(object):
    async def test_can_cancel(self, request_mock):
        resource = await stripe.Refund.retrieve(TEST_RESOURCE_ID)
        resource = await resource.cancel()
        request_mock.assert_requested(
            "post", "/v1/refund/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Quote)

    async def test_can_cancel_classmethod(self, request_mock):
        resource = await stripe.Refund.cancel(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/refund/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Quote)
