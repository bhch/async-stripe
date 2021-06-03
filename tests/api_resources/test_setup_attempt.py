from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio


class TestSetupAttempt(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.SetupAttempt.list(setup_intent="seti_123")
        request_mock.assert_requested("get", "/v1/setup_attempts")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.SetupAttempt)
