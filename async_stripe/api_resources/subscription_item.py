import stripe
from async_stripe.api_resources.abstract import patch_nested_resources


async def usage_record_summaries_patch(self, **params):
    """usage_record_summaries is deprecated, use SubscriptionItem.list_usage_record_summaries instead."""
    return await self.request(
        "get", self.instance_url() + "/usage_record_summaries", params
    )


stripe.SubscriptionItem.usage_record_summaries = usage_record_summaries_patch


nested_resources = ["usage_record", "usage_record_summary"]

patch_nested_resources(stripe.SubscriptionItem, nested_resources)