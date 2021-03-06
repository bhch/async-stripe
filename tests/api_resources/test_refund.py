from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio


TEST_RESOURCE_ID = "re_123"


class TestRefund(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.Refund.list()
        request_mock.assert_requested("get", "/v1/refunds")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Refund)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.Refund.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/refunds/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Refund)

    async def test_is_creatable(self, request_mock):
        resource = await stripe.Refund.create(charge="ch_123")
        request_mock.assert_requested("post", "/v1/refunds")
        assert isinstance(resource, stripe.Refund)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.Refund.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        await resource.save()
        request_mock.assert_requested(
            "post", "/v1/refunds/%s" % TEST_RESOURCE_ID
        )

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.Refund.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/refunds/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Refund)

    async def test_is_cancelable(self, request_mock):
        resource = await stripe.Refund.cancel(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/refunds/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Refund)

    async def test_refund_expire(self, request_mock):
        await stripe.Refund.TestHelpers.expire("re_123")
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/refunds/re_123/expire",
        )
