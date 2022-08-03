import stripe
from stripe import error
from stripe import util
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.account import Account
from stripe.api_resources.customer import Customer
from stripe.six.moves.urllib.parse import quote_plus


class Card(DeletableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "card"


async def modify_patch(cls, sid, **params):
    raise NotImplementedError(
        "Can't modify a card without a customer or account "
        "ID. Call save on customer.sources.retrieve('card_id'), or "
        "account.external_accounts.retrieve('card_id') instead."
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
        "Can't retrieve a card without a customer, or account "
        "ID. Use customer.sources.retrieve('card_id'), or"
        "account.external_accounts.retrieve('card_id') instead."
    )


stripe.Card.modify = classmethod(modify_patch)
stripe.Card.retrieve = classmethod(retrieve_patch)