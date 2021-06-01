from stripe import util
from async_stripe.api_requestor import AsyncAPIRequestor


def patch_nested_resources(cls, nested_resources):
    for resource in nested_resources:
        resource_plural = '%ss' % resource
        nested_resource_request_method = '%s_request' % resource_plural

        async def nested_resource_request(
            cls,
            method,
            url,
            api_key=None,
            idempotency_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
        ):
            requestor = AsyncAPIRequestor(
                api_key, api_version=stripe_version, account=stripe_account
            )
            headers = util.populate_headers(idempotency_key)
            response, api_key = await requestor.request(method, url, params, headers)
            return util.convert_to_stripe_object(
                response, api_key, stripe_version, stripe_account
            )
    
        setattr(cls, nested_resource_request_method, classmethod(nested_resource_request))