import stripe
from stripe import util
from stripe.api_resources.abstract import ListableAPIResource
from async_stripe.api_resources.abstract import patch_nested_resources


nested_resources = ["refund"]

patch_nested_resources(stripe.ApplicationFee, nested_resources)