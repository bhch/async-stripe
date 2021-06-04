import stripe


def modify_patch(cls, sid, **params):
    raise NotImplementedError(
        "Can't modify a reversal without a transfer"
        "ID. Call save on transfer.reversals.retrieve('reversal_id')"
    )


def retrieve_patch(cls, id, api_key=None, **params):
    raise NotImplementedError(
        "Can't retrieve a reversal without a transfer"
        "ID. Use transfer.reversals.retrieve('reversal_id')"
    )


stripe.Reversal.modify = classmethod(modify_patch)
stripe.Reversal.retrieve = classmethod(retrieve_patch)