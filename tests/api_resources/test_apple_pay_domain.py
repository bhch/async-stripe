from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "apwc_123"


class TestApplePayDomain(object):
    async def test_is_listable(self, request_mock):
        resources = await stripe.ApplePayDomain.list()
        request_mock.assert_requested("get", "/v1/apple_pay/domains")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.ApplePayDomain)

    async def test_is_retrievable(self, request_mock):
        resource = await stripe.ApplePayDomain.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/apple_pay/domains/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.ApplePayDomain)

    async def test_is_creatable(self, request_mock):
        resource = await stripe.ApplePayDomain.create(domain_name="test.com")
        request_mock.assert_requested("post", "/v1/apple_pay/domains")
        assert isinstance(resource, stripe.ApplePayDomain)

    async def test_is_deletable(self, request_mock):
        resource = await stripe.ApplePayDomain.retrieve(TEST_RESOURCE_ID)
        await resource.delete()
        request_mock.assert_requested(
            "delete", "/v1/apple_pay/domains/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    async def test_can_delete(self, request_mock):
        resource = await stripe.ApplePayDomain.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/apple_pay/domains/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
