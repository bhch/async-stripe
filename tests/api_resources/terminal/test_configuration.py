from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio


class TestConfiguration(object):
    async def test_terminal_configuration_list(self, request_mock):
        await stripe.terminal.Configuration.list()
        request_mock.assert_requested("get", "/v1/terminal/configurations")

    async def test_terminal_configuration_retrieve(self, request_mock):
        await stripe.terminal.Configuration.retrieve("uc_123")
        request_mock.assert_requested(
            "get", "/v1/terminal/configurations/uc_123"
        )

    async def test_terminal_configuration_create(self, request_mock):
        await stripe.terminal.Configuration.create()
        request_mock.assert_requested("post", "/v1/terminal/configurations")

    async def test_terminal_configuration_update(self, request_mock):
        await stripe.terminal.Configuration.modify(
            "uc_123",
            tipping={"usd": {"fixed_amounts": [10]}},
        )
        request_mock.assert_requested(
            "post", "/v1/terminal/configurations/uc_123"
        )

    async def test_terminal_configuration_delete(self, request_mock):
        await stripe.terminal.Configuration.delete("uc_123")
        request_mock.assert_requested(
            "delete",
            "/v1/terminal/configurations/uc_123",
        )
