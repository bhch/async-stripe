from stripe.api_resources.abstract import APIResource


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
            return await APIResource._static_request(
                method,
                url,
                api_key=api_key,
                idempotency_key=idempotency_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )
    
        setattr(cls, nested_resource_request_method, classmethod(nested_resource_request))