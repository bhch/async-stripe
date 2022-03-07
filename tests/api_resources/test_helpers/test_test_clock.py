from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio


class TestTestClock(object):
    async def test_test_helpers_testclock_create(self, request_mock):
        await stripe.test_helpers.TestClock.create(frozen_time=123, name="cogsworth")
        request_mock.assert_requested("post", "/v1/test_helpers/test_clocks")

    async def test_test_helpers_testclock_retrieve(self, request_mock):
        await stripe.test_helpers.TestClock.retrieve("clock_xyz")
        request_mock.assert_requested(
            "get",
            "/v1/test_helpers/test_clocks/clock_xyz",
        )

    async def test_test_helpers_testclock_list(self, request_mock):
        await stripe.test_helpers.TestClock.list()
        request_mock.assert_requested("get", "/v1/test_helpers/test_clocks")

    async def test_test_helpers_testclock_delete(self, request_mock):
        await stripe.test_helpers.TestClock.delete("clock_xyz")
        request_mock.assert_requested(
            "delete",
            "/v1/test_helpers/test_clocks/clock_xyz",
        )

    async def test_test_helpers_testclock_advance(self, request_mock):
        await stripe.test_helpers.TestClock.advance("clock_xyz", frozen_time=142)
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/test_clocks/clock_xyz/advance",
        )
