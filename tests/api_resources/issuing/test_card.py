from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "ic_123"


class TestCard(object):
    async def test_is_creatable(self, request_mock):
        resource = await stripe.issuing.Card.create(currency="usd", type="physical")
        request_mock.assert_requested("post", "/v1/issuing/cards")
        assert isinstance(resource, stripe.issuing.Card)

    async def test_is_listable(self, request_mock):
        resources = await stripe.issuing.Card.list()
        request_mock.assert_requested("get", "/v1/issuing/cards")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.issuing.Card)

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.issuing.Card.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/issuing/cards/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Card)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.issuing.Card.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/issuing/cards/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Card)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.issuing.Card.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        card = await resource.save()
        request_mock.assert_requested(
            "post", "/v1/issuing/cards/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Card)
        assert resource is card

    async def test_can_retrieve_details(self, request_mock):
        # stripe-mock does not handle this anymore so we stub instead.
        request_mock.stub_request(
            "get",
            "/v1/issuing/cards/%s/details" % TEST_RESOURCE_ID,
            {"object": "issuing.card_details"},
        )
        card = stripe.issuing.Card.construct_from(
            {"id": "%s" % TEST_RESOURCE_ID, "object": "issuing.card"},
            stripe.api_key,
        )
        card_details = await card.details()
        request_mock.assert_requested(
            "get", "/v1/issuing/cards/%s/details" % TEST_RESOURCE_ID
        )
        assert isinstance(card_details, stripe.issuing.CardDetails)

    async def test_can_retrieve_details_classmethod(self, request_mock):
        # stripe-mock does not handle this anymore so we stub instead.
        request_mock.stub_request(
            "get",
            "/v1/issuing/cards/%s/details" % TEST_RESOURCE_ID,
            {"object": "issuing.card_details"},
        )

        card_details = await stripe.issuing.Card.details(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/issuing/cards/%s/details" % TEST_RESOURCE_ID
        )
        assert isinstance(card_details, stripe.issuing.CardDetails)
