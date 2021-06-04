from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio


class TestDeletableAPIResource(object):
    class MyDeletable(stripe.api_resources.abstract.DeletableAPIResource):
        OBJECT_NAME = "mydeletable"

    async def test_delete_class(self, request_mock):
        request_mock.stub_request(
            "delete",
            "/v1/mydeletables/mid",
            {"id": "mid", "deleted": True},
            rheaders={"request-id": "req_id"},
        )

        obj = await self.MyDeletable.delete("mid")

        request_mock.assert_requested("delete", "/v1/mydeletables/mid", {})
        assert obj.deleted is True
        assert obj.id == "mid"

        assert obj.last_response is not None
        assert obj.last_response.request_id == "req_id"

    async def test_delete_class_with_object(self, request_mock):
        request_mock.stub_request(
            "delete",
            "/v1/mydeletables/mid",
            {"id": "mid", "deleted": True},
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyDeletable.construct_from({"id": "mid"}, "mykey")

        await self.MyDeletable.delete(obj)

        request_mock.assert_requested("delete", "/v1/mydeletables/mid", {})
        assert obj.deleted is True
        assert obj.id == "mid"

        assert obj.last_response is not None
        assert obj.last_response.request_id == "req_id"

    async def test_delete_instance(self, request_mock):
        request_mock.stub_request(
            "delete",
            "/v1/mydeletables/mid",
            {"id": "mid", "deleted": True},
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyDeletable.construct_from({"id": "mid"}, "mykey")

        assert obj is await obj.delete()
        request_mock.assert_requested("delete", "/v1/mydeletables/mid", {})
        assert obj.deleted is True
        assert obj.id == "mid"

        assert obj.last_response is not None
        assert obj.last_response.request_id == "req_id"
