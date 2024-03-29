from __future__ import absolute_import, division, print_function

import pytest

import stripe


pytestmark = pytest.mark.asyncio


class TestUpdateableAPIResource(object):
    class MyUpdateable(stripe.api_resources.abstract.UpdateableAPIResource):
        OBJECT_NAME = "myupdateable"

    @pytest.fixture
    async def obj(self, request_mock):
        request_mock.stub_request(
            "post",
            "/v1/myupdateables/myid",
            {"id": "myid", "thats": "it"},
            rheaders={"request-id": "req_id"},
        )

        return self.MyUpdateable.construct_from(
            {
                "id": "myid",
                "foo": "bar",
                "baz": "boz",
                "metadata": {"size": "l", "score": 4, "height": 10},
                "object": "obj",
            },
            "mykey",
        )

    async def checkSave(self, obj):
        assert obj is await obj.save()

        assert obj.thats == "it"
        # TODO: Should we force id to be retained?
        # assert obj.id == 'myid'
        with pytest.raises(AttributeError):
            obj.baz

    async def test_idempotent_save(self, request_mock, obj):
        obj.baz = "updated"
        await obj.save(idempotency_key="foo")

        request_mock.assert_requested(
            "post",
            "/v1/myupdateables/myid",
            {"baz": "updated"},
            {"Idempotency-Key": "foo"},
        )

    async def test_save(self, request_mock, obj):
        obj.baz = "updated"
        obj.other = "newval"
        obj.metadata.size = "m"
        obj.metadata.info = "a2"
        obj.metadata.height = None

        await self.checkSave(obj)

        request_mock.assert_requested(
            "post",
            "/v1/myupdateables/myid",
            {
                "baz": "updated",
                "other": "newval",
                "metadata": {"size": "m", "info": "a2", "height": ""},
            },
            None,
        )

        assert obj.last_response is not None
        assert obj.last_response.request_id == "req_id"

        # Saving again should not cause any request.
        request_mock.reset_mock()
        await self.checkSave(obj)
        request_mock.assert_no_request()

        # Setting the same value should cause a request.
        request_mock.stub_request(
            "post", "/v1/myupdateables/myid", {"id": "myid", "thats": "it"}
        )

        obj.thats = "it"
        await self.checkSave(obj)

        request_mock.assert_requested(
            "post", "/v1/myupdateables/myid", {"thats": "it"}, None
        )

        # Changing the value should cause a request.
        request_mock.stub_request(
            "post", "/v1/myupdateables/myid", {"id": "myid", "thats": "it"}
        )

        obj.id = "myid"
        obj.thats = "updated"
        await self.checkSave(obj)

        request_mock.assert_requested(
            "post", "/v1/myupdateables/myid", {"thats": "updated"}, None
        )

    async def test_add_key_to_nested_object(self, request_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {
                "id": "myid",
                "legal_entity": {"size": "l", "score": 4, "height": 10},
            },
            "mykey",
        )

        acct.legal_entity["first_name"] = "bob"

        assert acct is await acct.save()

        request_mock.assert_requested(
            "post",
            "/v1/myupdateables/myid",
            {"legal_entity": {"first_name": "bob"}},
            None,
        )

    async def test_save_nothing(self, request_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {"id": "myid", "metadata": {"key": "value"}}, "mykey"
        )

        assert acct is await acct.save()

        request_mock.assert_no_request()

    async def test_replace_nested_object(self, request_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {"id": "myid", "legal_entity": {"last_name": "smith"}}, "mykey"
        )

        acct.legal_entity = {"first_name": "bob"}

        assert acct is await acct.save()

        request_mock.assert_requested(
            "post",
            "/v1/myupdateables/myid",
            {"legal_entity": {"first_name": "bob", "last_name": ""}},
            None,
        )

    async def test_array_setting(self, request_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {"id": "myid", "legal_entity": {}}, "mykey"
        )

        acct.legal_entity.additional_owners = [{"first_name": "Bob"}]

        assert acct is await acct.save()

        request_mock.assert_requested(
            "post",
            "/v1/myupdateables/myid",
            {"legal_entity": {"additional_owners": [{"first_name": "Bob"}]}},
            None,
        )

    async def test_array_none(self, request_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {"id": "myid", "legal_entity": {"additional_owners": None}},
            "mykey",
        )

        acct.foo = "bar"

        assert acct is await acct.save()

        request_mock.assert_requested(
            "post", "/v1/myupdateables/myid", {"foo": "bar"}, None
        )

    async def test_array_insertion(self, request_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {"id": "myid", "legal_entity": {"additional_owners": []}}, "mykey"
        )

        acct.legal_entity.additional_owners.append({"first_name": "Bob"})

        assert acct is await acct.save()

        request_mock.assert_requested(
            "post",
            "/v1/myupdateables/myid",
            {
                "legal_entity": {
                    "additional_owners": {"0": {"first_name": "Bob"}}
                }
            },
            None,
        )

    async def test_array_update(self, request_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {
                "id": "myid",
                "legal_entity": {
                    "additional_owners": [
                        {"first_name": "Bob"},
                        {"first_name": "Jane"},
                    ]
                },
            },
            "mykey",
        )

        acct.legal_entity.additional_owners[1].first_name = "Janet"

        assert acct is await acct.save()

        request_mock.assert_requested(
            "post",
            "/v1/myupdateables/myid",
            {
                "legal_entity": {
                    "additional_owners": {
                        "0": {},
                        "1": {"first_name": "Janet"},
                    }
                }
            },
            None,
        )

    async def test_array_noop(self, request_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {
                "id": "myid",
                "legal_entity": {"additional_owners": [{"first_name": "Bob"}]},
                "currencies_supported": ["usd", "cad"],
            },
            "mykey",
        )

        assert acct is await acct.save()

        request_mock.assert_requested(
            "post",
            "/v1/myupdateables/myid",
            {"legal_entity": {"additional_owners": {"0": {}}}},
            None,
        )

    async def test_hash_noop(self, request_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {
                "id": "myid",
                "legal_entity": {"address": {"line1": "1 Two Three"}},
            },
            "mykey",
        )

        assert acct is await acct.save()

        request_mock.assert_no_request()

    async def test_save_replace_metadata_with_number(self, request_mock, obj):
        obj.baz = "updated"
        obj.other = "newval"
        obj.metadata = 3

        await self.checkSave(obj)

        request_mock.assert_requested(
            "post",
            "/v1/myupdateables/myid",
            {"baz": "updated", "other": "newval", "metadata": 3},
            None,
        )

    async def test_save_overwrite_metadata(self, request_mock, obj):
        obj.metadata = {}
        await self.checkSave(obj)

        request_mock.assert_requested(
            "post",
            "/v1/myupdateables/myid",
            {"metadata": {"size": "", "score": "", "height": ""}},
            None,
        )

    async def test_save_replace_metadata(self, request_mock, obj):
        obj.baz = "updated"
        obj.other = "newval"
        obj.metadata = {"size": "m", "info": "a2", "score": 4}

        await self.checkSave(obj)

        request_mock.assert_requested(
            "post",
            "/v1/myupdateables/myid",
            {
                "baz": "updated",
                "other": "newval",
                "metadata": {
                    "size": "m",
                    "info": "a2",
                    "height": "",
                    "score": 4,
                },
            },
            None,
        )

    async def test_save_update_metadata(self, request_mock, obj):
        obj.baz = "updated"
        obj.other = "newval"
        obj.metadata.update({"size": "m", "info": "a2", "score": 4})

        await self.checkSave(obj)

        request_mock.assert_requested(
            "post",
            "/v1/myupdateables/myid",
            {
                "baz": "updated",
                "other": "newval",
                "metadata": {"size": "m", "info": "a2", "score": 4},
            },
            None,
        )

    async def test_retrieve_and_update_with_stripe_version(self, request_mock, obj):
        request_mock.stub_request(
            "get", "/v1/myupdateables/foo", {"id": "foo", "bobble": "scrobble"}
        )

        res = await self.MyUpdateable.retrieve("foo", stripe_version="2017-08-15")

        request_mock.assert_api_version("2017-08-15")

        request_mock.stub_request(
            "post",
            "/v1/myupdateables/foo",
            {"id": "foo", "bobble": "new_scrobble"},
        )

        res.bobble = "new_scrobble"
        await res.save()

        request_mock.assert_api_version("2017-08-15")

    async def test_modify_with_all_special_fields(self, request_mock, obj):
        request_mock.stub_request(
            "post",
            "/v1/myupdateables/foo",
            {"id": "foo", "bobble": "new_scrobble"},
            {"Idempotency-Key": "IdempotencyKey"},
        )

        await self.MyUpdateable.modify(
            "foo",
            stripe_version="2017-08-15",
            api_key="APIKEY",
            idempotency_key="IdempotencyKey",
            stripe_account="Acc",
            bobble="new_scrobble",
            headers={"extra_header": "val"},
        )

        request_mock.assert_requested(
            "post",
            "/v1/myupdateables/foo",
            {"bobble": "new_scrobble"},
            {"Idempotency-Key": "IdempotencyKey", "extra_header": "val"},
        )
        request_mock.assert_api_version("2017-08-15")
