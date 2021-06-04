from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "pts_123"


class TestSession(object):
    async def test_is_creatable(self, request_mock):
        resource = await stripe.billing_portal.Session.create(
            customer="cus_123", return_url="https://stripe.com/return"
        )
        request_mock.assert_requested("post", "/v1/billing_portal/sessions")
        assert isinstance(resource, stripe.billing_portal.Session)
