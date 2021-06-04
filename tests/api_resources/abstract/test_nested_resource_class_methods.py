from __future__ import absolute_import, division, print_function

import stripe

import pytest

from async_stripe.api_resources.abstract import patch_nested_resources


pytestmark = pytest.mark.asyncio


class TestNestedResourceClassMethods(object):
    @stripe.api_resources.abstract.nested_resource_class_methods(
        "nested", operations=["create", "retrieve", "update", "delete", "list"]
    )
    class MainResource(stripe.api_resources.abstract.APIResource):
        OBJECT_NAME = "mainresource"

    patch_nested_resources(MainResource, ["nested"])

    async def test_create_nested(self, request_mock):
        request_mock.stub_request(
            "post",
            "/v1/mainresources/id/nesteds",
            {"id": "nested_id", "object": "nested", "foo": "bar"},
        )
        nested_resource = await self.MainResource.create_nested("id", foo="bar")
        request_mock.assert_requested(
            "post", "/v1/mainresources/id/nesteds", {"foo": "bar"}, None
        )
        assert nested_resource.foo == "bar"

    async def test_retrieve_nested(self, request_mock):
        request_mock.stub_request(
            "get",
            "/v1/mainresources/id/nesteds/nested_id",
            {"id": "nested_id", "object": "nested", "foo": "bar"},
        )
        nested_resource = await self.MainResource.retrieve_nested("id", "nested_id")
        request_mock.assert_requested(
            "get", "/v1/mainresources/id/nesteds/nested_id", {}, None
        )
        assert nested_resource.foo == "bar"

    async def test_modify_nested(self, request_mock):
        request_mock.stub_request(
            "post",
            "/v1/mainresources/id/nesteds/nested_id",
            {"id": "nested_id", "object": "nested", "foo": "baz"},
        )
        nested_resource = await self.MainResource.modify_nested(
            "id", "nested_id", foo="baz"
        )
        request_mock.assert_requested(
            "post",
            "/v1/mainresources/id/nesteds/nested_id",
            {"foo": "baz"},
            None,
        )
        assert nested_resource.foo == "baz"

    async def test_delete_nested(self, request_mock):
        request_mock.stub_request(
            "delete",
            "/v1/mainresources/id/nesteds/nested_id",
            {"id": "nested_id", "object": "nested", "deleted": True},
        )
        nested_resource = await self.MainResource.delete_nested("id", "nested_id")
        request_mock.assert_requested(
            "delete", "/v1/mainresources/id/nesteds/nested_id", {}, None
        )
        assert nested_resource.deleted is True

    async def test_list_nesteds(self, request_mock):
        request_mock.stub_request(
            "get",
            "/v1/mainresources/id/nesteds",
            {"object": "list", "data": []},
        )
        nested_resource = await self.MainResource.list_nesteds("id")
        request_mock.assert_requested(
            "get", "/v1/mainresources/id/nesteds", {}, None
        )
        assert isinstance(nested_resource.data, list)
