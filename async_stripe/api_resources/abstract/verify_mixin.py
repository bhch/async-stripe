from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract.verify_mixin import VerifyMixin
from stripe import util


async def verify_patch(self, idempotency_key=None, **params):
    url = self.instance_url() + "/verify"
    headers = util.populate_headers(idempotency_key)
    self.refresh_from(await self.request("post", url, params, headers))
    return self


VerifyMixin.verify = verify_patch