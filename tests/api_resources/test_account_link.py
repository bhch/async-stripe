from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio


class TestAccountLink(object):
    async def test_is_creatable(self, request_mock):
        resource = await stripe.AccountLink.create(
            account="acct_123",
            refresh_url="https://stripe.com/failure",
            return_url="https://stripe.com/success",
            type="account_onboarding",
        )
        request_mock.assert_requested("post", "/v1/account_links")
        assert isinstance(resource, stripe.AccountLink)
