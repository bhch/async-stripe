from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio


class TestBalance(object):
    async def test_is_retrievable(self, request_mock):
        resource = await stripe.Balance.retrieve()
        request_mock.assert_requested("get", "/v1/balance")
        assert isinstance(resource, stripe.Balance)
