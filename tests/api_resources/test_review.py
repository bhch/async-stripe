from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "prv_123"


class TestReview(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.Review.list()
        request_mock.assert_requested("get", "/v1/reviews")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Review)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.Review.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/reviews/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Review)

    async def test_can_approve(self, request_mock):
        resource = await stripe.Review.retrieve(TEST_RESOURCE_ID)
        await resource.approve()
        request_mock.assert_requested(
            "post", "/v1/reviews/%s/approve" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Review)

    async def test_can_approve_classmethod(self, request_mock):
        resource = await stripe.Review.approve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/reviews/%s/approve" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Review)
