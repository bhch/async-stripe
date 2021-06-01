from stripe import util
from stripe.six.moves.urllib.parse import quote_plus
from stripe.api_resources.abstract.deletable_api_resource import (
    DeletableAPIResource,
)
from async_stripe.api_requestor import AsyncAPIRequestor


async def _cls_delete_patch(cls, sid, **params):
    url = "%s/%s" % (cls.class_url(), quote_plus(util.utf8(sid)))
    return await cls._static_request("delete", url, **params)

@util.class_method_variant("_cls_delete")
async def delete_patch(self, **params):
    self.refresh_from(await self.request("delete", self.instance_url(), params))


for subclass in DeletableAPIResource.__subclasses__():
    subclass._cls_delete = classmethod(_cls_delete_patch)
    subclass.delete = delete_patch