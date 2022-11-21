# -*- coding: utf-8 -*-
import stripe


async def modify_patch(cls, sid, **params):
    raise NotImplementedError(
        "Can't modify a card without a customer or account ID. "
        "Use stripe.Customer.modify_source('customer_id', 'card_id', ...) "
        "(see https://stripe.com/docs/api/cards/update) or "
        "stripe.Account.modify_external_account('account_id', 'card_id', ...) "
        "(see https://stripe.com/docs/api/external_account_cards/update)."
    )


async def retrieve_patch(
    cls,
    id,
    api_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    raise NotImplementedError(
        "Can't retrieve a card without a customer or account ID. "
        "Use stripe.Customer.retrieve_source('customer_id', 'card_id') "
        "(see https://stripe.com/docs/api/cards/retrieve) or "
        "stripe.Account.retrieve_external_account('account_id', 'card_id') "
        "(see https://stripe.com/docs/api/external_account_cards/retrieve)."
    )


stripe.Card.modify = classmethod(modify_patch)
stripe.Card.retrieve = classmethod(retrieve_patch)
