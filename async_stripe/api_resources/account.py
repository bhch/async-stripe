import stripe
from stripe import oauth, six
from stripe import util
from stripe.six.moves.urllib.parse import quote_plus
from async_stripe.api_resources.abstract import (
    patch_custom_methods, patch_nested_resources
)


async def reject_patch(self, idempotency_key=None, **params):
    url = "/v1/accounts/{account}/reject".format(
        account=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


async def retrieve_patch(cls, id=None, api_key=None, **params):
    instance = cls(id, api_key, **params)
    await instance.refresh()
    return instance


async def modify_patch(cls, id=None, **params):
    url = cls._build_instance_url(id)
    return await cls._static_request("post", url, **params)


async def persons_patch(self, idempotency_key=None, **params):
    url = "/v1/accounts/{account}/persons".format(
        account=util.sanitize_id(self.get("id"))
    )
    headers = util.populate_headers(idempotency_key)
    resp = await self.request("get", url, params, headers)
    stripe_object = util.convert_to_stripe_object(resp)
    stripe_object._retrieve_params = params
    return stripe_object


async def deauthorize_patch(self, **params):
    params["stripe_user_id"] = self.id
    return await oauth.OAuth.deauthorize(**params)


stripe.Account.reject = reject_patch
stripe.Account.retrieve = classmethod(retrieve_patch)
stripe.Account.modify = classmethod(modify_patch)
stripe.Account.persons = persons_patch
stripe.Account.deauthorize = deauthorize_patch


def serialize_patch(self, previous):
    params = super(Account, self).serialize(previous)
    previous = previous or self._previous or {}

    for k, v in six.iteritems(self):
        if (
            k == "individual"
            and isinstance(v, stripe.api_resources.Person)
            and k not in params
        ):
            params[k] = v.serialize(previous.get(k, None))

    return params


nested_resources = ["capability", "login_link", "external_account", "person",]

patch_nested_resources(stripe.Account, nested_resources)


custom_methods = [
    {"name": "reject", "http_verb": "post"},
    {"name": "persons", "http_verb": "get"},
]

patch_custom_methods(stripe.Account, custom_methods)