from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio


class TestCreateableAPIResource(object):
    class MyCreatable(stripe.api_resources.abstract.CreateableAPIResource):
        OBJECT_NAME = "mycreatable"

    async def test_create(self, request_mock):
        request_mock.stub_request(
            "post",
            "/v1/mycreatables",
            {"object": "charge", "foo": "bar"},
            rheaders={"request-id": "req_id"},
        )

        res = await self.MyCreatable.create()

        request_mock.assert_requested("post", "/v1/mycreatables", {})
        assert isinstance(res, stripe.Charge)
        assert res.foo == "bar"

        assert res.last_response is not None
        assert res.last_response.request_id == "req_id"

    async def test_idempotent_create(self, request_mock):
        request_mock.stub_request(
            "post",
            "/v1/mycreatables",
            {"object": "charge", "foo": "bar"},
            rheaders={"idempotency-key": "foo"},
        )

        res = await self.MyCreatable.create(idempotency_key="foo")

        request_mock.assert_requested(
            "post", "/v1/mycreatables", {}, {"Idempotency-Key": "foo"}
        )
        assert isinstance(res, stripe.Charge)
        assert res.foo == "bar"
