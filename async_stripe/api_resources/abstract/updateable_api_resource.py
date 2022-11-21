from stripe import util
from stripe.six.moves.urllib.parse import quote_plus
from stripe.api_resources.abstract.updateable_api_resource import (
    UpdateableAPIResource,
)


async def save_patch(self, idempotency_key=None):
    """
    The `save` method is deprecated and will be removed in a future major version of the library.
    Use the class method `modify` on the resource instead.
    """
    updated_params = self.serialize(None)

    if updated_params:
        await self._request_and_refresh(
            "post",
            self.instance_url(),
            idempotency_key=idempotency_key,
            params=updated_params,
        )
    else:
        util.logger.debug("Trying to save already saved object %r", self)
    return self


UpdateableAPIResource.save = save_patch


for subclass in UpdateableAPIResource.__subclasses__():
    subclass.save = save_patch