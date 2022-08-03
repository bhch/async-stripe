import stripe


async def retrieve_patch(cls, id, api_key=None, **params):
    raise NotImplementedError(
        "Can't retrieve a refund without an application fee ID. "
        "Use application_fee.refunds.retrieve('refund_id') instead."
    )


stripe.ApplicationFeeRefund.retrieve = classmethod(retrieve_patch)
