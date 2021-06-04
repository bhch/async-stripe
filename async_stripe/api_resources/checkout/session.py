import stripe
from async_stripe.api_resources.abstract import patch_nested_resources


nested_resources = ["line_item"]

patch_nested_resources(stripe.checkout.Session, nested_resources)