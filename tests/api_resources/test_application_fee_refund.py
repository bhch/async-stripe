from __future__ import absolute_import, division, print_function

import pytest

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "fr_123"
TEST_APPFEE_ID = "fee_123"


class TestApplicationFeeRefund(object):
    async def test_is_saveable(self, request_mock):
        appfee = await stripe.ApplicationFee.retrieve(TEST_APPFEE_ID)
        resource = await appfee.refunds.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        await resource.save()
        request_mock.assert_requested(
            "post",
            "/v1/application_fees/%s/refunds/%s"
            % (TEST_APPFEE_ID, TEST_RESOURCE_ID),
        )

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.ApplicationFeeRefund.modify(
            TEST_APPFEE_ID, TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post",
            "/v1/application_fees/%s/refunds/%s"
            % (TEST_APPFEE_ID, TEST_RESOURCE_ID),
        )
        assert isinstance(resource, stripe.ApplicationFeeRefund)

    async def test_is_not_retrievable(self):
        with pytest.raises(NotImplementedError):
            await stripe.ApplicationFeeRefund.retrieve(TEST_RESOURCE_ID)
