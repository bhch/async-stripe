from stripe import util
from stripe import api_requestor


def patch_nested_resources(cls, nested_resources):
    for resource in nested_resources:
        nested_resource_request_method = '%ss_request' % resource

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
            requestor = api_requestor.APIRequestor(
                api_key, api_version=stripe_version, account=stripe_account
            )
            headers = util.populate_headers(idempotency_key)
            response, api_key = await requestor.request(method, url, params, headers)
            return util.convert_to_stripe_object(
                response, api_key, stripe_version, stripe_account
            )
    
        setattr(cls, nested_resource_request_method, classmethod(nested_resource_request))