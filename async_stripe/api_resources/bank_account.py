# -*- coding: utf-8 -*-
import stripe


async def modify_patch(cls, sid, **params):
    raise NotImplementedError(
        "Can't modify a bank account without a customer or account ID. "
        "Use stripe.Customer.modify_source('customer_id', 'bank_account_id', ...) "
        "(see https://stripe.com/docs/api/customer_bank_accounts/update) or "
        "stripe.Account.modify_external_account('customer_id', 'bank_account_id', ...) "
        "(see https://stripe.com/docs/api/external_account_bank_accounts/update)."
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
        "Use stripe.customer.retrieve_source('customer_id', 'bank_account_id') "
        "(see https://stripe.com/docs/api/customer_bank_accounts/retrieve) or "
        "stripe.Account.retrieve_external_account('account_id', 'bank_account_id') "
        "(see https://stripe.com/docs/api/external_account_bank_accounts/retrieve)."
    )


stripe.BankAccount.modify = classmethod(modify_patch)
stripe.BankAccount.retrieve = classmethod(retrieve_patch)