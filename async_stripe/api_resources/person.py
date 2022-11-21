# -*- coding: utf-8 -*-
import stripe


async def modify_patch(cls, sid, **params):
    raise NotImplementedError(
        "Can't modify a person without an account ID. "
        "Use stripe.Account.modify_person('account_id', 'person_id', ...) "
        "(see https://stripe.com/docs/api/persons/update)."
    )


async def retrieve_patch(cls, id, api_key=None, **params):
    raise NotImplementedError(
        "Can't retrieve a person without an account ID. "
        "Use stripe.Account.retrieve_person('account_id', 'person_id') "
        "(see https://stripe.com/docs/api/persons/retrieve)."
    )


stripe.Person.modify = classmethod(modify_patch)
stripe.Person.retrieve = classmethod(retrieve_patch)