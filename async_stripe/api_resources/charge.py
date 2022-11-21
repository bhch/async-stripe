# -*- coding: utf-8 -*-
import stripe
from stripe import util


async def mark_as_fraudulent_patch(self, idempotency_key=None):
    params = {"fraud_details": {"user_report": "fraudulent"}}
    url = self.instance_url()
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self

async def mark_as_safe_patch(self, idempotency_key=None):
    params = {"fraud_details": {"user_report": "safe"}}
    url = self.instance_url()
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


stripe.Charge.mark_as_fraudulent = mark_as_fraudulent_patch
stripe.Charge.mark_as_safe = mark_as_safe_patch
