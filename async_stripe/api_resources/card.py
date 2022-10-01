import stripe


async def modify_patch(cls, sid, **params):
    raise NotImplementedError(
        "Can't modify a card without a customer or account "
        "ID. Call save on customer.sources.retrieve('card_id'), or "
        "account.external_accounts.retrieve('card_id') instead."
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
        "Can't retrieve a card without a customer, or account "
        "ID. Use customer.sources.retrieve('card_id'), or"
        "account.external_accounts.retrieve('card_id') instead."
    )


stripe.Card.modify = classmethod(modify_patch)
stripe.Card.retrieve = classmethod(retrieve_patch)
