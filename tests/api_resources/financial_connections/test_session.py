from __future__ import absolute_import, division, print_function

import stripe

import pytest

pytestmark = pytest.mark.asyncio


TEST_RESOURCE_ID = "fca_123"


class TestSession(object):
    async def test_financial_connections_session_create(self, request_mock):
        await stripe.financial_connections.Session.create(
            account_holder={"type": "customer", "customer": "cus_123"},
            permissions=["balances"],
        )
        request_mock.assert_requested(
            "post", "/v1/financial_connections/sessions"
        )

    async def test_financial_connections_session_retrieve(self, request_mock):
        await stripe.financial_connections.Session.retrieve("fcsess_xyz")
        request_mock.assert_requested(
            "get",
            "/v1/financial_connections/sessions/fcsess_xyz",
        )
