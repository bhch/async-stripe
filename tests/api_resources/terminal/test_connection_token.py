from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "rdr_123"


class TestConnectionToken(object):
    async def test_is_creatable(self, request_mock):
        resource = await stripe.terminal.ConnectionToken.create()
        request_mock.assert_requested("post", "/v1/terminal/connection_tokens")
        assert isinstance(resource, stripe.terminal.ConnectionToken)
