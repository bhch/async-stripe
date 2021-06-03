import stripe
from stripe import util


async def modify_patch(cls, customer, id, **params):
    url = cls._build_instance_url(customer, id)
    return await cls._static_request("post", url, **params)


async def retrieve_patch(
    cls,
    id,
    api_key=None,
    stripe_version=None,
    stripe_account=None,
    **params
):
    raise NotImplementedError(
        "Can't retrieve an Alipay account without a customer ID. "
        "Use customer.sources.retrieve('alipay_account_id') instead."
    )


stripe.AlipayAccount.modify = classmethod(modify_patch)
stripe.AlipayAccount.retrieve = classmethod(retrieve_patch)