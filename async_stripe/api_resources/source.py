# -*- coding: utf-8 -*-
import stripe
from stripe import error
from stripe import util
from stripe.api_resources import Customer
from urllib.parse import quote_plus


async def detach_patch(self, idempotency_key=None, **params):
    token = self.id

    if hasattr(self, "customer") and self.customer:
        extn = quote_plus(token)
        customer = self.customer
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


stripe.Source.detach = detach_patch
