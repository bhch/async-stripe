from __future__ import absolute_import, division, print_function

import pytest

import stripe


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "src_123"


class TestSource(object):
    async def test_is_retrievable(self, request_mock):
        resource = await stripe.Source.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/sources/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Source)

    async def test_is_creatable(self, request_mock):
        resource = await stripe.Source.create(type="card", token="tok_123")
        request_mock.assert_requested("post", "/v1/sources")
        assert isinstance(resource, stripe.Source)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.Source.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        await resource.save()
        request_mock.assert_requested(
            "post", "/v1/sources/%s" % TEST_RESOURCE_ID
        )

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.Source.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/sources/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Source)

    async def test_is_detachable_when_attached(self, request_mock):
        resource = stripe.Source.construct_from(
            {
                "id": TEST_RESOURCE_ID,
                "object": "source",
                "customer": "cus_123",
            },
            stripe.api_key,
        )
        source = await resource.detach()
        assert source is resource
        request_mock.assert_requested(
            "delete", "/v1/customers/cus_123/sources/%s" % TEST_RESOURCE_ID
        )

    async def test_is_not_detachable_when_unattached(self, request_mock):
        resource = await stripe.Source.retrieve(TEST_RESOURCE_ID)
        with pytest.raises(stripe.error.InvalidRequestError):
            await resource.detach()

    async def test_is_verifiable(self, request_mock):
        resource = await stripe.Source.retrieve(TEST_RESOURCE_ID)
        source = await resource.verify(values=[1, 2])
        assert source is resource
        request_mock.assert_requested(
            "post",
            "/v1/sources/%s/verify" % TEST_RESOURCE_ID,
            {"values": [1, 2]},
        )


class TestSourceTransactions(object):
    async def test_is_listable(self, request_mock):
        resource = await stripe.Source.list_source_transactions(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/sources/%s/source_transactions" % TEST_RESOURCE_ID
        )
        assert isinstance(resource.data, list)
        assert isinstance(resource.data[0], stripe.SourceTransaction)
