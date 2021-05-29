from .base import AsyncBaseResource, BASE_URL

class AsyncPaymentMethod(AsyncBaseResource):
    resource = 'PaymentMethod'
    url = BASE_URL + 'payment_methods'  


class AsyncPaymentIntent(AsyncBaseResource):
    resource = 'PaymentIntent'
    url = BASE_URL + 'payment_intents'


class AsyncCustomer(AsyncBaseResource):
    resource = 'Customer'
    url = BASE_URL + 'customers'
    