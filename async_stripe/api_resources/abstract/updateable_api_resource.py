from stripe import util
from stripe.six.moves.urllib.parse import quote_plus
from stripe.api_resources.abstract.updateable_api_resource import (
    UpdateableAPIResource,
)


async def modify_patch(cls, sid, **params):
    url = "%s/%s" % (cls.class_url(), quote_plus(util.utf8(sid)))
    return await cls._static_request("post", url, **params)


async def save_patch(self, idempotency_key=None):
    updated_params = self.serialize(None)
    headers = util.populate_headers(idempotency_key)

    if updated_params:
        self.refresh_from(
            await self.request(
                "post", self.instance_url(), updated_params, headers
            )
        )
    else:
        util.logger.debug("Trying to save already saved object %r", self)
    return self


UpdateableAPIResource.modify = classmethod(modify_patch)
UpdateableAPIResource.save = save_patch


for subclass in UpdateableAPIResource.__subclasses__():
    subclass.modify = classmethod(modify_patch)
    subclass.save = save_patch