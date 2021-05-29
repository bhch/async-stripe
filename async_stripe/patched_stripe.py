import stripe as real_stripe
from .resources import (
    AsyncPaymentMethod, AsyncPaymentIntent, AsyncCustomer
    )

class Stripe:
    PaymentMethod = AsyncPaymentMethod
    PaymentIntent = AsyncPaymentIntent
    Customer = AsyncCustomer

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        setattr(real_stripe, name, value)

    def __getattr__(self, name):
            return getattr(real_stripe, name)


stripe = Stripe()
