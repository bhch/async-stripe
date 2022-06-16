from __future__ import absolute_import, division, print_function

import stripe

import pytest

pytestmark = pytest.mark.asyncio


TEST_RESOURCE_ID = "fca_123"


class TestAccount(object):
    async def test_financial_connections_account_refresh_account(self, request_mock):
        await stripe.financial_connections.Account.refresh_account(
            "fca_xyz",
            features=["balance"],
        )
        request_mock.assert_requested(
            "post",
            "/v1/financial_connections/accounts/fca_xyz/refresh",
        )

    async def test_financial_connections_account_disconnect(self, request_mock):
        await stripe.financial_connections.Account.disconnect("fca_xyz")
        request_mock.assert_requested(
            "post",
            "/v1/financial_connections/accounts/fca_xyz/disconnect",
        )
