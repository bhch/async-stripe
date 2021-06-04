import stripe


async def modify_patch(cls, sid, **params):
    raise NotImplementedError(
        "Can't update a capability without an account ID. Update a capability using "
        "account.modify_capability('acct_123', 'acap_123', params)"
    )

async def retrieve_patch(cls, id, api_key=None, **params):
    raise NotImplementedError(
        "Can't retrieve a capability without an account ID. Retrieve a capability using "
        "account.retrieve_capability('acct_123', 'acap_123')"
    )


stripe.Capability.modify = classmethod(modify_patch)
stripe.Capability.retrieve = classmethod(retrieve_patch)