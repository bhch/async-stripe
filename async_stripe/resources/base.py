import json
from urllib.parse import urlencode
from tornado.httpclient import AsyncHTTPClient, HTTPError
from stripe.api_requestor import _api_encode
from async_stripe.patched_stripe import real_stripe


BASE_URL = 'https://api.stripe.com/v1/'


client = AsyncHTTPClient()


class ResourceMetaclass(type):
    def __getattr__(cls, name):
        resource = getattr(real_stripe, cls.resource)
        return getattr(resource, name)


class AsyncBaseResource(metaclass=ResourceMetaclass):
    @classmethod
    async def fetch(cls, url, method='GET', data=None):
        if data:
            body = urlencode(list(_api_encode(data)), doseq=True)
        else:
            body = None

        try:
            response = await client.fetch(
                url,
                method=method,
                auth_username=real_stripe.api_key,
                body=body
            )
        except HTTPError as e:
            # :TODO: log exception
            if hasattr(e, 'response'):
                print('ERROR:', e.code)
                print(e.response.body)
            raise
        except Exception as e:
            # :TODO: log exception
            raise
        else:
            obj = real_stripe.util.convert_to_stripe_object(json.loads(response.body), real_stripe.api_key)
            return obj

    @classmethod
    async def retrieve(cls, id):
        url = cls.url + '/' + id
        obj = await cls.fetch(url)
        return obj

    @classmethod
    async def create(cls, **kwargs):
        url = cls.url
        obj = await cls.fetch(url, method='POST', data=kwargs)
        return obj

    @classmethod
    async def modify(cls, id, **kwargs):
        url = cls.url + '/' + id
        obj = await cls.fetch(url, method='POST', data=kwargs)
        return obj

