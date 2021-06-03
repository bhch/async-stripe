import stripe


async def modify_patch(cls, fee, sid, **params):
    url = cls._build_instance_url(fee, sid)
    return await cls._static_request("post", url, **params)


async def retrieve_patch(cls, id, api_key=None, **params):
    raise NotImplementedError(
        "Can't retrieve a refund without an application fee ID. "
        "Use application_fee.refunds.retrieve('refund_id') instead."
    )


stripe.ApplicationFeeRefund.modify = classmethod(modify_patch)
stripe.ApplicationFeeRefund.retrieve = classmethod(retrieve_patch)