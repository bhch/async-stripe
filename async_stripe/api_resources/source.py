import stripe
from stripe import error
from stripe import util
from stripe.api_resources import Customer
from stripe.six.moves.urllib.parse import quote_plus
from async_stripe.api_resources.abstract import patch_nested_resources


async def detach_patch(self, idempotency_key=None, **params):
    token = util.utf8(self.id)

    if hasattr(self, "customer") and self.customer:
        extn = quote_plus(token)
        customer = util.utf8(self.customer)
        base = Customer.class_url()
        owner_extn = quote_plus(customer)
        url = "%s/%s/sources/%s" % (base, owner_extn, extn)
        headers = util.populate_headers(idempotency_key)

        self.refresh_from(await self.request("delete", url, params, headers))
        return self

    else:
        raise error.InvalidRequestError(
            "Source %s does not appear to be currently attached "
            "to a customer object." % token,
            "id",
        )


async def source_transactions_patch(self, **params):
    """source_transactions is deprecated, use Source.list_source_transactions instead."""
    return await self.request(
        "get", self.instance_url() + "/source_transactions", params
    )


stripe.Source.detach = detach_patch
stripe.Source.source_transactions = source_transactions_patch


nested_resources = ["source_transaction"]

patch_nested_resources(stripe.Source, nested_resources)