from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "ipi_123"


class TestTransaction(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.issuing.Transaction.list()
        request_mock.assert_requested("get", "/v1/issuing/transactions")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.issuing.Transaction)

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.issuing.Transaction.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/issuing/transactions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Transaction)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.issuing.Transaction.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/issuing/transactions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Transaction)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.issuing.Transaction.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        transaction = await resource.save()
        request_mock.assert_requested(
            "post", "/v1/issuing/transactions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Transaction)
        assert resource is transaction
