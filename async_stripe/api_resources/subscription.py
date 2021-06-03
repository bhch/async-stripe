import stripe
from stripe import api_requestor
from async_stripe.api_resources.abstract import patch_custom_methods


async def delete_discount_patch(self, **params):
    requestor = api_requestor.APIRequestor(
        self.api_key,
        api_version=self.stripe_version,
        account=self.stripe_account,
    )
    url = self.instance_url() + "/discount"
    _, api_key = await requestor.request("delete", url, params)
    self.refresh_from({"discount": None}, api_key, True)


stripe.Subscription.delete_discount = delete_discount_patch


custom_methods = [
    {"name": "delete_discount", "http_verb": "delete", "http_path": "discount"}
]

patch_custom_methods(stripe.Subscription, custom_methods)