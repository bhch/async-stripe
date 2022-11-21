# -*- coding: utf-8 -*-
import stripe


def modify_patch(cls, sid, **params):
    raise NotImplementedError(
        "Can't modify a reversal without a transfer ID. "
        "Use stripe.Transfer.modify_reversal('transfer_id', 'reversal_id', ...) "
        "(see https://stripe.com/docs/api/transfer_reversals/update)."
    )


def retrieve_patch(cls, id, api_key=None, **params):
    raise NotImplementedError(
        "Can't retrieve a reversal without a transfer ID. "
        "Use stripe.Transfer.retrieve_reversal('transfer_id', 'reversal_id') "
        "(see https://stripe.com/docs/api/transfer_reversals/retrieve)."
    )


stripe.Reversal.modify = classmethod(modify_patch)
stripe.Reversal.retrieve = classmethod(retrieve_patch)