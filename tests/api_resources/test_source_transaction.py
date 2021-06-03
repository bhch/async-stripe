from __future__ import absolute_import, division, print_function

import stripe

import pytest


pytestmark = pytest.mark.asyncio


class TestSourceTransaction(object):
    async def test_is_listable(self, request_mock):
        source = stripe.Source.construct_from(
            {"id": "src_123", "object": "source"}, stripe.api_key
        )
        source_transactions = await source.source_transactions()
        request_mock.assert_requested(
            "get", "/v1/sources/src_123/source_transactions"
        )
        assert isinstance(source_transactions.data, list)
        assert isinstance(
            source_transactions.data[0], stripe.SourceTransaction
        )
