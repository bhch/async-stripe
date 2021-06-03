from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "iauth_123"


class TestAuthorization(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.issuing.Authorization.list()
        request_mock.assert_requested("get", "/v1/issuing/authorizations")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.issuing.Authorization)

    async def test_is_modifiable(self, request_mock):
        resource = await stripe.issuing.Authorization.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/issuing/authorizations/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Authorization)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.issuing.Authorization.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/issuing/authorizations/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Authorization)

    async def test_is_saveable(self, request_mock):
        resource = await stripe.issuing.Authorization.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        authorization = await resource.save()
        request_mock.assert_requested(
            "post", "/v1/issuing/authorizations/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Authorization)
        assert resource is authorization

    async def test_can_approve(self, request_mock):
        resource = await stripe.issuing.Authorization.retrieve(TEST_RESOURCE_ID)
        authorization = await resource.approve()
        request_mock.assert_requested(
            "post", "/v1/issuing/authorizations/%s/approve" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Authorization)
        assert resource is authorization

    async def test_can_approve_classmethod(self, request_mock):
        resource = await stripe.issuing.Authorization.approve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/issuing/authorizations/%s/approve" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Authorization)

    async def test_can_decline(self, request_mock):
        resource = await stripe.issuing.Authorization.retrieve(TEST_RESOURCE_ID)
        authorization = await resource.decline()
        request_mock.assert_requested(
            "post", "/v1/issuing/authorizations/%s/decline" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Authorization)
        assert resource is authorization

    async def test_can_decline_classmethod(self, request_mock):
        resource = await stripe.issuing.Authorization.decline(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/issuing/authorizations/%s/decline" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Authorization)
