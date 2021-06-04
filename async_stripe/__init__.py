import stripe

# register this library as a plugin
stripe.set_app_info('async-stripe', url='https://github.com/bhch/async-stripe')

# import monkey patches
from async_stripe import stripe_object
from async_stripe import http_client
from async_stripe import api_requestor
from async_stripe import api_resources
from async_stripe import oauth