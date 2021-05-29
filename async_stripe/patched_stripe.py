import stripe as real_stripe
from .resources import (
    AsyncPaymentMethod, AsyncPaymentIntent, AsyncCustomer
    )

class Stripe:
    def __init__(self):
        self._api_key = None
        self._public_key = None
        self._webhook_secret = None

    PaymentMethod = AsyncPaymentMethod
    PaymentIntent = AsyncPaymentIntent
    Customer = AsyncCustomer

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, value):
        self._api_key = value
        real_stripe.api_key = value

    def __getattr__(self, name):
            return getattr(real_stripe, name)


stripe = Stripe()
