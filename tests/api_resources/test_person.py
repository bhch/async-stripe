from __future__ import absolute_import, division, print_function

import pytest

import stripe


pytestmark = pytest.mark.asyncio

TEST_RESOURCE_ID = "trr_123"


class TestPerson(object):
    def construct_resource(self):
        person_dict = {
            "id": TEST_RESOURCE_ID,
            "object": "person",
            "account": "acct_123",
        }
        return stripe.Person.construct_from(person_dict, stripe.api_key)

    async def test_has_instance_url(self, request_mock):
        resource = self.construct_resource()
        assert (
            resource.instance_url()
            == "/v1/accounts/acct_123/persons/%s" % TEST_RESOURCE_ID
        )

    async def test_is_not_modifiable(self, request_mock):
        with pytest.raises(NotImplementedError):
            await stripe.Person.modify(TEST_RESOURCE_ID, first_name="John")

    async def test_is_not_retrievable(self, request_mock):
        with pytest.raises(NotImplementedError):
            await stripe.Person.retrieve(TEST_RESOURCE_ID)

    async def test_is_saveable(self, request_mock):
        resource = self.construct_resource()
        resource.first_name = "John"
        await resource.save()
        request_mock.assert_requested(
            "post", "/v1/accounts/acct_123/persons/%s" % TEST_RESOURCE_ID
        )
