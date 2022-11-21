# -*- coding: utf-8 -*-
import stripe
from async_stripe.api_resources.abstract import patch_nested_resources
from stripe import util


netsted_resources = ['balance_transaction', 'cash_balance_transaction', 'source', 'tax_id']
patch_nested_resources(stripe.Customer, netsted_resources)
