from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio


class TestUsageRecordSummary(object):
    async def test_is_listable(self, request_mock):
        resource = await stripe.SubscriptionItem.retrieve("si_123")
        usage_record_summaries = await resource.usage_record_summaries()
        request_mock.assert_requested(
            "get", "/v1/subscription_items/si_123/usage_record_summaries"
        )
        assert isinstance(usage_record_summaries.data, list)
        assert isinstance(
            usage_record_summaries.data[0], stripe.UsageRecordSummary
        )
