from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "fee_123"
TEST_FEEREFUND_ID = "fr_123"


class TestApplicationFee(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.ApplicationFee.list()
        request_mock.assert_requested("get", "/v1/application_fees")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.ApplicationFee)

    async def test_is_refundable(self, request_mock):
        appfee = await stripe.ApplicationFee.retrieve(TEST_RESOURCE_ID)
        resource = await appfee.refund()
        request_mock.assert_requested(
            "post", "/v1/application_fees/%s/refund" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.ApplicationFee)
        assert resource is appfee


class TestApplicationFeeRefunds(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.ApplicationFee.list_refunds(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/application_fees/%s/refunds" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.ApplicationFeeRefund)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.ApplicationFee.retrieve_refund(
            TEST_RESOURCE_ID, TEST_FEEREFUND_ID
        )
        request_mock.assert_requested(
            "get",
            "/v1/application_fees/%s/refunds/%s"
            % (TEST_RESOURCE_ID, TEST_FEEREFUND_ID),
        )
        assert isinstance(resource, stripe.ApplicationFeeRefund)

    async def test_is_creatable(self, request_mock):
        resource = await stripe.ApplicationFee.create_refund(
            TEST_RESOURCE_ID, amount=100
        )
        request_mock.assert_requested(
            "post", "/v1/application_fees/%s/refunds" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.ApplicationFeeRefund)

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.ApplicationFee.modify_refund(
            TEST_RESOURCE_ID, TEST_FEEREFUND_ID, metadata={"foo": "bar"}
        )
        request_mock.assert_requested(
            "post",
            "/v1/application_fees/%s/refunds/%s"
            % (TEST_RESOURCE_ID, TEST_FEEREFUND_ID),
        )
        assert isinstance(resource, stripe.ApplicationFeeRefund)
