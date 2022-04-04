from stripe import error, util, six
from stripe.six.moves.urllib.parse import quote_plus
from stripe.api_resources.abstract.test_helpers import APIResourceTestHelpers
from async_stripe.api_resources.abstract.api_resource import APIResource


# Some resource classes have a nested TestHelpers class
# but they still have some unpatched methods
for subclass in APIResourceTestHelpers.__subclasses__():
    subclass._static_request = subclass._resource_cls._static_request
    subclass._static_request_stream = subclass._resource_cls._static_request_stream
