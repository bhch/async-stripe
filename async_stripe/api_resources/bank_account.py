import stripe


async def modify_patch(cls, sid, **params):
    raise NotImplementedError(
        "Can't modify a bank account without a customer or account ID. "
        "Call save on customer.sources.retrieve('bank_account_id') or "
        "account.external_accounts.retrieve('bank_account_id') instead."
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
        "Can't retrieve a bank account without a customer or account ID. "
        "Use customer.sources.retrieve('bank_account_id') or "
        "account.external_accounts.retrieve('bank_account_id') instead."
    )


stripe.BankAccount.modify = classmethod(modify_patch)
stripe.BankAccount.retrieve = classmethod(retrieve_patch)