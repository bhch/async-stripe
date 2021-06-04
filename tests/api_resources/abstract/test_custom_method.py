from __future__ import absolute_import, division, print_function

import stripe

import pytest

from stripe import util


pytestmark = pytest.mark.asyncio


class TestCustomMethod(object):
    @stripe.api_resources.abstract.custom_method(
        "do_stuff", http_verb="post", http_path="do_the_thing"
    )
    class MyResource(stripe.api_resources.abstract.APIResource):
        OBJECT_NAME = "myresource"

        async def do_stuff(self, idempotency_key=None, **params):
            url = self.instance_url() + "/do_the_thing"
            headers = util.populate_headers(idempotency_key)
            self.refresh_from(await self.request("post", url, params, headers))
            return self

    async def test_call_custom_method_class(self, request_mock):
        request_mock.stub_request(
            "post",
            "/v1/myresources/mid/do_the_thing",
            {"id": "mid", "thing_done": True},
            rheaders={"request-id": "req_id"},
        )

        obj = await self.MyResource.do_stuff("mid", foo="bar")

        request_mock.assert_requested(
            "post", "/v1/myresources/mid/do_the_thing", {"foo": "bar"}
        )
        assert obj.thing_done is True

    async def test_call_custom_method_class_with_object(self, request_mock):
        request_mock.stub_request(
            "post",
            "/v1/myresources/mid/do_the_thing",
            {"id": "mid", "thing_done": True},
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyResource.construct_from({"id": "mid"}, "mykey")
        await self.MyResource.do_stuff(obj, foo="bar")

        request_mock.assert_requested(
            "post", "/v1/myresources/mid/do_the_thing", {"foo": "bar"}
        )
        assert obj.thing_done is True

    async def test_call_custom_method_instance(self, request_mock):
        request_mock.stub_request(
            "post",
            "/v1/myresources/mid/do_the_thing",
            {"id": "mid", "thing_done": True},
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyResource.construct_from({"id": "mid"}, "mykey")
        await obj.do_stuff(foo="bar")

        request_mock.assert_requested(
            "post", "/v1/myresources/mid/do_the_thing", {"foo": "bar"}
        )
        assert obj.thing_done is True