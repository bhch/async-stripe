import stripe


async def modify_patch(cls, sid, **params):
    raise NotImplementedError(
        "Can't modify a person without an account"
        "ID. Call save on account.persons.retrieve('person_id')"
    )


async def retrieve_patch(cls, id, api_key=None, **params):
    raise NotImplementedError(
        "Can't retrieve a person without an account"
        "ID. Use account.persons.retrieve('person_id')"
    )


stripe.Person.modify = classmethod(modify_patch)
stripe.Person.retrieve = classmethod(retrieve_patch)