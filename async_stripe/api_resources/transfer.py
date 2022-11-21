# -*- coding: utf-8 -*-
import stripe
from stripe import util
from async_stripe.api_resources.abstract import patch_nested_resources


netsted_resources = ["reversal"]
patch_nested_resources(stripe.Transfer, netsted_resources)
