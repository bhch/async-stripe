# -*- coding: utf-8 -*-
import stripe
from stripe import oauth, six
from stripe import util
from stripe.six.moves.urllib.parse import quote_plus
from async_stripe.api_resources.abstract import patch_nested_resources


async def retrieve_patch(cls, id=None, api_key=None, **params):
    instance = cls(id, api_key, **params)
    await instance.refresh()
    return instance


stripe.Account.retrieve = classmethod(retrieve_patch)


nested_resources = ["capability", "login_link", "external_account", "person",]

patch_nested_resources(stripe.Account, nested_resources)
