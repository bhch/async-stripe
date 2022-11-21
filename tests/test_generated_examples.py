from __future__ import absolute_import, division, print_function

import pytest
import stripe


pytestmark = pytest.mark.asyncio


class TestGeneratedExamples(object):
    async def test_apps_secret_list(self, request_mock):
        await stripe.apps.Secret.list(scope={"type": "account"}, limit=2)
        request_mock.assert_requested("get", "/v1/apps/secrets")

    async def test_apps_secret_create(self, request_mock):
        await stripe.apps.Secret.create(
            name="sec_123",
            payload="very secret string",
            scope={"type": "account"},
        )
        request_mock.assert_requested("post", "/v1/apps/secrets")

    async def test_apps_secret_delete_where(self, request_mock):
        await stripe.apps.Secret.delete_where(
            name="my-api-key",
            scope={"type": "account"},
        )
        request_mock.assert_requested("post", "/v1/apps/secrets/delete")

    async def test_apps_secret_find(self, request_mock):
        await stripe.apps.Secret.find(name="sec_123", scope={"type": "account"})
        request_mock.assert_requested("get", "/v1/apps/secrets/find")

    async def test_checkout_session_create(self, request_mock):
        await stripe.checkout.Session.create(
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
            mode="payment",
            shipping_options=[
                {"shipping_rate": "shr_standard"},
                {
                    "shipping_rate_data": {
                        "display_name": "Standard",
                        "delivery_estimate": {
                            "minimum": {"unit": "day", "value": 5},
                            "maximum": {"unit": "day", "value": 7},
                        },
                    },
                },
            ],
        )
        request_mock.assert_requested("post", "/v1/checkout/sessions")

    async def test_checkout_session_expire(self, request_mock):
        await stripe.checkout.Session.expire("sess_xyz")
        request_mock.assert_requested(
            "post",
            "/v1/checkout/sessions/sess_xyz/expire",
        )

    async def test_checkout_session_list_line_items(self, request_mock):
        await stripe.checkout.Session.list_line_items("sess_xyz")
        request_mock.assert_requested(
            "get",
            "/v1/checkout/sessions/sess_xyz/line_items",
        )

    async def test_customer_cashbalance_retrieve(self, request_mock):
        await stripe.Customer.retrieve_cash_balance("cus_123")
        request_mock.assert_requested(
            "get", "/v1/customers/cus_123/cash_balance"
        )

    async def test_customer_cashbalance_update(self, request_mock):
        await stripe.Customer.modify_cash_balance(
            "cus_123",
            settings={"reconciliation_mode": "manual"},
        )
        request_mock.assert_requested(
            "post", "/v1/customers/cus_123/cash_balance"
        )

    async def test_customer_create_funding_instructions(self, request_mock):
        await stripe.Customer.create_funding_instructions(
            "cus_123",
            bank_transfer={
                "requested_address_types": ["zengin"],
                "type": "jp_bank_transfer",
            },
            currency="usd",
            funding_type="bank_transfer",
        )
        request_mock.assert_requested(
            "post",
            "/v1/customers/cus_123/funding_instructions",
        )

    async def test_customer_list_payment_methods(self, request_mock):
        await stripe.Customer.list_payment_methods("cus_xyz", type="card")
        request_mock.assert_requested(
            "get",
            "/v1/customers/cus_xyz/payment_methods",
        )

    async def test_financial_connections_account_list(self, request_mock):
        await stripe.financial_connections.Account.list()
        request_mock.assert_requested(
            "get", "/v1/financial_connections/accounts"
        )

    async def test_financial_connections_account_retrieve(self, request_mock):
        await stripe.financial_connections.Account.retrieve("fca_xyz")
        request_mock.assert_requested(
            "get",
            "/v1/financial_connections/accounts/fca_xyz",
        )

    async def test_financial_connections_account_disconnect(self, request_mock):
        await stripe.financial_connections.Account.disconnect("fca_xyz")
        request_mock.assert_requested(
            "post",
            "/v1/financial_connections/accounts/fca_xyz/disconnect",
        )

    async def test_financial_connections_account_list_owners(self, request_mock):
        await stripe.financial_connections.Account.list_owners(
            "fca_xyz",
            ownership="fcaowns_xyz",
        )
        request_mock.assert_requested(
            "get",
            "/v1/financial_connections/accounts/fca_xyz/owners",
        )

    async def test_financial_connections_account_refresh_account(self, request_mock):
        await stripe.financial_connections.Account.refresh_account(
            "fca_xyz",
            features=["balance"],
        )
        request_mock.assert_requested(
            "post",
            "/v1/financial_connections/accounts/fca_xyz/refresh",
        )

    async def test_financial_connections_session_create(self, request_mock):
        await stripe.financial_connections.Session.create(
            account_holder={"type": "customer", "customer": "cus_123"},
            permissions=["balances"],
        )
        request_mock.assert_requested(
            "post", "/v1/financial_connections/sessions"
        )

    async def test_financial_connections_session_retrieve(self, request_mock):
        await stripe.financial_connections.Session.retrieve("fcsess_xyz")
        request_mock.assert_requested(
            "get",
            "/v1/financial_connections/sessions/fcsess_xyz",
        )

    async def test_invoice_upcoming(self, request_mock):
        await stripe.Invoice.upcoming(customer="cus_9utnxg47pWjV1e")
        request_mock.assert_requested("get", "/v1/invoices/upcoming")

    async def test_paymentintent_create(self, request_mock):
        await stripe.PaymentIntent.create(
            amount=1099,
            currency="eur",
            automatic_payment_methods={"enabled": True},
        )
        request_mock.assert_requested("post", "/v1/payment_intents")

    async def test_paymentintent_verify_microdeposits(self, request_mock):
        await stripe.PaymentIntent.verify_microdeposits("pi_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents/pi_xxxxxxxxxxxxx/verify_microdeposits",
        )

    async def test_paymentlink_create(self, request_mock):
        await stripe.PaymentLink.create(
            line_items=[{"price": "price_xxxxxxxxxxxxx", "quantity": 1}],
        )
        request_mock.assert_requested("post", "/v1/payment_links")

    async def test_paymentlink_retrieve(self, request_mock):
        await stripe.PaymentLink.retrieve("pl_xyz")
        request_mock.assert_requested("get", "/v1/payment_links/pl_xyz")

    async def test_paymentlink_list_line_items(self, request_mock):
        await stripe.PaymentLink.list_line_items("pl_xyz")
        request_mock.assert_requested(
            "get", "/v1/payment_links/pl_xyz/line_items"
        )

    async def test_price_create(self, request_mock):
        await stripe.Price.create(
            unit_amount=2000,
            currency="usd",
            currency_options={
                "uah": {"unit_amount": 5000},
                "eur": {"unit_amount": 1800},
            },
            recurring={"interval": "month"},
            product="prod_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested("post", "/v1/prices")

    async def test_setupattempt_list(self, request_mock):
        await stripe.SetupAttempt.list(limit=3, setup_intent="si_xyz")
        request_mock.assert_requested("get", "/v1/setup_attempts")

    async def test_setupintent_verify_microdeposits(self, request_mock):
        await stripe.SetupIntent.verify_microdeposits("seti_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/setup_intents/seti_xxxxxxxxxxxxx/verify_microdeposits",
        )

    async def test_shippingrate_list(self, request_mock):
        await stripe.ShippingRate.list()
        request_mock.assert_requested("get", "/v1/shipping_rates")

    async def test_shippingrate_create(self, request_mock):
        await stripe.ShippingRate.create(
            display_name="Sample Shipper",
            fixed_amount={"currency": "usd", "amount": 400},
            type="fixed_amount",
        )
        request_mock.assert_requested("post", "/v1/shipping_rates")

    async def test_terminal_configuration_list(self, request_mock):
        await stripe.terminal.Configuration.list()
        request_mock.assert_requested("get", "/v1/terminal/configurations")

    async def test_terminal_configuration_create(self, request_mock):
        await stripe.terminal.Configuration.create()
        request_mock.assert_requested("post", "/v1/terminal/configurations")

    async def test_terminal_configuration_delete(self, request_mock):
        await stripe.terminal.Configuration.delete("uc_123")
        request_mock.assert_requested(
            "delete",
            "/v1/terminal/configurations/uc_123",
        )

    async def test_terminal_configuration_retrieve(self, request_mock):
        await stripe.terminal.Configuration.retrieve("uc_123")
        request_mock.assert_requested(
            "get", "/v1/terminal/configurations/uc_123"
        )

    async def test_terminal_configuration_update(self, request_mock):
        await stripe.terminal.Configuration.modify(
            "uc_123",
            tipping={"usd": {"fixed_amounts": [10]}},
        )
        request_mock.assert_requested(
            "post", "/v1/terminal/configurations/uc_123"
        )

    async def test_customer_fund_cash_balance(self, request_mock):
        await stripe.Customer.TestHelpers.fund_cash_balance(
            "cus_123",
            amount=30,
            currency="eur",
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/customers/cus_123/fund_cash_balance",
        )

    async def test_issuing_card_deliver_card(self, request_mock):
        await stripe.issuing.Card.TestHelpers.deliver_card("card_123")
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/issuing/cards/card_123/shipping/deliver",
        )

    async def test_issuing_card_fail_card(self, request_mock):
        await stripe.issuing.Card.TestHelpers.fail_card("card_123")
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/issuing/cards/card_123/shipping/fail",
        )

    async def test_issuing_card_return_card(self, request_mock):
        await stripe.issuing.Card.TestHelpers.return_card("card_123")
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/issuing/cards/card_123/shipping/return",
        )

    async def test_issuing_card_ship_card(self, request_mock):
        await stripe.issuing.Card.TestHelpers.ship_card("card_123")
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/issuing/cards/card_123/shipping/ship",
        )

    async def test_refund_expire(self, request_mock):
        await stripe.Refund.TestHelpers.expire("re_123")
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/refunds/re_123/expire",
        )

    async def test_test_helpers_testclock_list(self, request_mock):
        await stripe.test_helpers.TestClock.list()
        request_mock.assert_requested("get", "/v1/test_helpers/test_clocks")

    async def test_test_helpers_testclock_create(self, request_mock):
        await stripe.test_helpers.TestClock.create(frozen_time=123, name="cogsworth")
        request_mock.assert_requested("post", "/v1/test_helpers/test_clocks")

    async def test_test_helpers_testclock_delete(self, request_mock):
        await stripe.test_helpers.TestClock.delete("clock_xyz")
        request_mock.assert_requested(
            "delete",
            "/v1/test_helpers/test_clocks/clock_xyz",
        )

    async def test_test_helpers_testclock_retrieve(self, request_mock):
        await stripe.test_helpers.TestClock.retrieve("clock_xyz")
        request_mock.assert_requested(
            "get",
            "/v1/test_helpers/test_clocks/clock_xyz",
        )

    async def test_test_helpers_testclock_advance(self, request_mock):
        await stripe.test_helpers.TestClock.advance("clock_xyz", frozen_time=142)
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/test_clocks/clock_xyz/advance",
        )

    async def test_treasury_inboundtransfer_fail(self, request_mock):
        await stripe.treasury.InboundTransfer.TestHelpers.fail(
            "ibt_123",
            failure_details={"code": "account_closed"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/treasury/inbound_transfers/ibt_123/fail",
        )

    async def test_treasury_inboundtransfer_return_inbound_transfer(
        self, request_mock
    ):
        await stripe.treasury.InboundTransfer.TestHelpers.return_inbound_transfer(
            "ibt_123",
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/treasury/inbound_transfers/ibt_123/return",
        )

    async def test_treasury_inboundtransfer_succeed(self, request_mock):
        await stripe.treasury.InboundTransfer.TestHelpers.succeed("ibt_123")
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/treasury/inbound_transfers/ibt_123/succeed",
        )

    async def test_treasury_outboundtransfer_fail(self, request_mock):
        await stripe.treasury.OutboundTransfer.TestHelpers.fail("obt_123")
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/treasury/outbound_transfers/obt_123/fail",
        )

    async def test_treasury_outboundtransfer_post(self, request_mock):
        await stripe.treasury.OutboundTransfer.TestHelpers.post("obt_123")
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/treasury/outbound_transfers/obt_123/post",
        )

    async def test_treasury_outboundtransfer_return_outbound_transfer(
        self, request_mock
    ):
        await stripe.treasury.OutboundTransfer.TestHelpers.return_outbound_transfer(
            "obt_123",
            returned_details={"code": "account_closed"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/treasury/outbound_transfers/obt_123/return",
        )

    async def test_treasury_receivedcredit_create(self, request_mock):
        await stripe.treasury.ReceivedCredit.TestHelpers.create(
            financial_account="fa_123",
            network="ach",
            amount=1234,
            currency="usd",
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/treasury/received_credits",
        )

    async def test_treasury_receiveddebit_create(self, request_mock):
        await stripe.treasury.ReceivedDebit.TestHelpers.create(
            financial_account="fa_123",
            network="ach",
            amount=1234,
            currency="usd",
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/treasury/received_debits",
        )

    async def test_token_create(self, request_mock):
        await stripe.Token.create(
            card={
                "number": "4242424242424242",
                "exp_month": "5",
                "exp_year": "2023",
                "cvc": "314",
            },
        )
        request_mock.assert_requested("post", "/v1/tokens")

    async def test_accountlink_create(self, request_mock):
        await stripe.AccountLink.create(
            account="acct_xxxxxxxxxxxxx",
            refresh_url="https://example.com/reauth",
            return_url="https://example.com/return",
            type="account_onboarding",
        )
        request_mock.assert_requested("post", "/v1/account_links")

    async def test_account_list(self, request_mock):
        await stripe.Account.list(limit=3)
        request_mock.assert_requested("get", "/v1/accounts")

    async def test_account_create(self, request_mock):
        await stripe.Account.create(
            type="custom",
            country="US",
            email="jenny.rosen@example.com",
            capabilities={
                "card_payments": {"requested": True},
                "transfers": {"requested": True},
            },
        )
        request_mock.assert_requested("post", "/v1/accounts")

    async def test_account_delete(self, request_mock):
        await stripe.Account.delete("acct_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete", "/v1/accounts/acct_xxxxxxxxxxxxx"
        )

    async def test_account_retrieve(self, request_mock):
        await stripe.Account.retrieve("acct_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/accounts/acct_xxxxxxxxxxxxx")

    async def test_account_update(self, request_mock):
        await stripe.Account.modify(
            "acct_xxxxxxxxxxxxx", metadata={"order_id": "6735"}
        )
        request_mock.assert_requested(
            "post", "/v1/accounts/acct_xxxxxxxxxxxxx"
        )

    async def test_account_reject(self, request_mock):
        await stripe.Account.reject("acct_xxxxxxxxxxxxx", reason="fraud")
        request_mock.assert_requested(
            "post",
            "/v1/accounts/acct_xxxxxxxxxxxxx/reject",
        )

    async def test_account_capability_retrieve(self, request_mock):
        await stripe.Account.retrieve_capability(
            "acct_xxxxxxxxxxxxx", "card_payments"
        )
        request_mock.assert_requested(
            "get",
            "/v1/accounts/acct_xxxxxxxxxxxxx/capabilities/card_payments",
        )

    async def test_account_capability_update(self, request_mock):
        await stripe.Account.modify_capability(
            "acct_xxxxxxxxxxxxx",
            "card_payments",
            requested=True,
        )
        request_mock.assert_requested(
            "post",
            "/v1/accounts/acct_xxxxxxxxxxxxx/capabilities/card_payments",
        )

    async def test_account_person_retrieve(self, request_mock):
        await stripe.Account.retrieve_person(
            "acct_xxxxxxxxxxxxx", "person_xxxxxxxxxxxxx"
        )
        request_mock.assert_requested(
            "get",
            "/v1/accounts/acct_xxxxxxxxxxxxx/persons/person_xxxxxxxxxxxxx",
        )

    async def test_account_person_update(self, request_mock):
        await stripe.Account.modify_person(
            "acct_xxxxxxxxxxxxx",
            "person_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/accounts/acct_xxxxxxxxxxxxx/persons/person_xxxxxxxxxxxxx",
        )

    async def test_applicationfee_list(self, request_mock):
        await stripe.ApplicationFee.list(limit=3)
        request_mock.assert_requested("get", "/v1/application_fees")

    async def test_applicationfee_retrieve(self, request_mock):
        await stripe.ApplicationFee.retrieve("fee_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/application_fees/fee_xxxxxxxxxxxxx",
        )

    async def test_applicationfee_feerefund_retrieve(self, request_mock):
        await stripe.ApplicationFee.retrieve_refund(
            "fee_xxxxxxxxxxxxx",
            "fr_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "get",
            "/v1/application_fees/fee_xxxxxxxxxxxxx/refunds/fr_xxxxxxxxxxxxx",
        )

    async def test_applicationfee_feerefund_update(self, request_mock):
        await stripe.ApplicationFee.modify_refund(
            "fee_xxxxxxxxxxxxx",
            "fr_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/application_fees/fee_xxxxxxxxxxxxx/refunds/fr_xxxxxxxxxxxxx",
        )

    async def test_apps_secret_create2(self, request_mock):
        await stripe.apps.Secret.create(
            name="my-api-key",
            payload="secret_key_xxxxxx",
            scope={"type": "account"},
        )
        request_mock.assert_requested("post", "/v1/apps/secrets")

    async def test_balancetransaction_list(self, request_mock):
        await stripe.BalanceTransaction.list(limit=3)
        request_mock.assert_requested("get", "/v1/balance_transactions")

    async def test_balancetransaction_retrieve(self, request_mock):
        await stripe.BalanceTransaction.retrieve("txn_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/balance_transactions/txn_xxxxxxxxxxxxx",
        )

    async def test_billing_portal_configuration_list(self, request_mock):
        await stripe.billing_portal.Configuration.list(limit=3)
        request_mock.assert_requested(
            "get", "/v1/billing_portal/configurations"
        )

    async def test_billing_portal_configuration_create(self, request_mock):
        await stripe.billing_portal.Configuration.create(
            features={
                "customer_update": {
                    "allowed_updates": ["email", "tax_id"],
                    "enabled": True,
                },
                "invoice_history": {"enabled": True},
            },
            business_profile={
                "privacy_policy_url": "https://example.com/privacy",
                "terms_of_service_url": "https://example.com/terms",
            },
        )
        request_mock.assert_requested(
            "post", "/v1/billing_portal/configurations"
        )

    async def test_billing_portal_configuration_retrieve(self, request_mock):
        await stripe.billing_portal.Configuration.retrieve("bpc_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/billing_portal/configurations/bpc_xxxxxxxxxxxxx",
        )

    async def test_billing_portal_configuration_update(self, request_mock):
        await stripe.billing_portal.Configuration.modify(
            "bpc_xxxxxxxxxxxxx",
            business_profile={
                "privacy_policy_url": "https://example.com/privacy",
                "terms_of_service_url": "https://example.com/terms",
            },
        )
        request_mock.assert_requested(
            "post",
            "/v1/billing_portal/configurations/bpc_xxxxxxxxxxxxx",
        )

    async def test_billing_portal_session_create(self, request_mock):
        await stripe.billing_portal.Session.create(
            customer="cus_xxxxxxxxxxxxx",
            return_url="https://example.com/account",
        )
        request_mock.assert_requested("post", "/v1/billing_portal/sessions")

    async def test_charge_list(self, request_mock):
        await stripe.Charge.list(limit=3)
        request_mock.assert_requested("get", "/v1/charges")

    async def test_charge_create(self, request_mock):
        await stripe.Charge.create(
            amount=2000,
            currency="usd",
            source="tok_xxxx",
            description="My First Test Charge (created for API docs)",
        )
        request_mock.assert_requested("post", "/v1/charges")

    async def test_charge_retrieve(self, request_mock):
        await stripe.Charge.retrieve("ch_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/charges/ch_xxxxxxxxxxxxx")

    async def test_charge_update(self, request_mock):
        await stripe.Charge.modify("ch_xxxxxxxxxxxxx", metadata={"order_id": "6735"})
        request_mock.assert_requested("post", "/v1/charges/ch_xxxxxxxxxxxxx")

    async def test_charge_capture(self, request_mock):
        await stripe.Charge.capture("ch_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/charges/ch_xxxxxxxxxxxxx/capture",
        )

    async def test_charge_search(self, request_mock):
        await stripe.Charge.search(
            query="amount>999 AND metadata['order_id']:'6735'"
        )
        request_mock.assert_requested("get", "/v1/charges/search")

    async def test_checkout_session_list(self, request_mock):
        await stripe.checkout.Session.list(limit=3)
        request_mock.assert_requested("get", "/v1/checkout/sessions")

    async def test_checkout_session_create2(self, request_mock):
        await stripe.checkout.Session.create(
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
            line_items=[{"price": "price_xxxxxxxxxxxxx", "quantity": 2}],
            mode="payment",
        )
        request_mock.assert_requested("post", "/v1/checkout/sessions")

    async def test_checkout_session_retrieve(self, request_mock):
        await stripe.checkout.Session.retrieve("cs_test_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/checkout/sessions/cs_test_xxxxxxxxxxxxx",
        )

    async def test_checkout_session_expire2(self, request_mock):
        await stripe.checkout.Session.expire("cs_test_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/checkout/sessions/cs_test_xxxxxxxxxxxxx/expire",
        )

    async def test_countryspec_list(self, request_mock):
        await stripe.CountrySpec.list(limit=3)
        request_mock.assert_requested("get", "/v1/country_specs")

    async def test_countryspec_retrieve(self, request_mock):
        await stripe.CountrySpec.retrieve("US")
        request_mock.assert_requested("get", "/v1/country_specs/US")

    async def test_coupon_list(self, request_mock):
        await stripe.Coupon.list(limit=3)
        request_mock.assert_requested("get", "/v1/coupons")

    async def test_coupon_create(self, request_mock):
        await stripe.Coupon.create(
            percent_off=25.5,
            duration="repeating",
            duration_in_months=3,
        )
        request_mock.assert_requested("post", "/v1/coupons")

    async def test_coupon_delete(self, request_mock):
        await stripe.Coupon.delete("Z4OV52SU")
        request_mock.assert_requested("delete", "/v1/coupons/Z4OV52SU")

    async def test_coupon_retrieve(self, request_mock):
        await stripe.Coupon.retrieve("Z4OV52SU")
        request_mock.assert_requested("get", "/v1/coupons/Z4OV52SU")

    async def test_coupon_update(self, request_mock):
        await stripe.Coupon.modify("Z4OV52SU", metadata={"order_id": "6735"})
        request_mock.assert_requested("post", "/v1/coupons/Z4OV52SU")

    async def test_creditnote_list(self, request_mock):
        await stripe.CreditNote.list(limit=3)
        request_mock.assert_requested("get", "/v1/credit_notes")

    async def test_creditnote_create(self, request_mock):
        await stripe.CreditNote.create(
            invoice="in_xxxxxxxxxxxxx",
            lines=[
                {
                    "type": "invoice_line_item",
                    "invoice_line_item": "il_xxxxxxxxxxxxx",
                    "quantity": 1,
                },
            ],
        )
        request_mock.assert_requested("post", "/v1/credit_notes")

    async def test_creditnote_void_credit_note(self, request_mock):
        await stripe.CreditNote.void_credit_note("cn_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/credit_notes/cn_xxxxxxxxxxxxx/void",
        )

    async def test_creditnote_preview(self, request_mock):
        await stripe.CreditNote.preview(
            invoice="in_xxxxxxxxxxxxx",
            lines=[
                {
                    "type": "invoice_line_item",
                    "invoice_line_item": "il_xxxxxxxxxxxxx",
                    "quantity": 1,
                },
            ],
        )
        request_mock.assert_requested("get", "/v1/credit_notes/preview")

    async def test_customer_list(self, request_mock):
        await stripe.Customer.list(limit=3)
        request_mock.assert_requested("get", "/v1/customers")

    async def test_customer_list2(self, request_mock):
        await stripe.Customer.list(limit=3)
        request_mock.assert_requested("get", "/v1/customers")

    async def test_customer_create(self, request_mock):
        await stripe.Customer.create(
            description="My First Test Customer (created for API docs)",
        )
        request_mock.assert_requested("post", "/v1/customers")

    async def test_customer_delete(self, request_mock):
        await stripe.Customer.delete("cus_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete", "/v1/customers/cus_xxxxxxxxxxxxx"
        )

    async def test_customer_retrieve(self, request_mock):
        await stripe.Customer.retrieve("cus_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/customers/cus_xxxxxxxxxxxxx")

    async def test_customer_update(self, request_mock):
        await stripe.Customer.modify(
            "cus_xxxxxxxxxxxxx", metadata={"order_id": "6735"}
        )
        request_mock.assert_requested(
            "post", "/v1/customers/cus_xxxxxxxxxxxxx"
        )

    async def test_customer_customerbalancetransaction_retrieve(self, request_mock):
        await stripe.Customer.retrieve_balance_transaction(
            "cus_xxxxxxxxxxxxx",
            "cbtxn_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "get",
            "/v1/customers/cus_xxxxxxxxxxxxx/balance_transactions/cbtxn_xxxxxxxxxxxxx",
        )

    async def test_customer_list_payment_methods2(self, request_mock):
        await stripe.Customer.list_payment_methods("cus_xxxxxxxxxxxxx", type="card")
        request_mock.assert_requested(
            "get",
            "/v1/customers/cus_xxxxxxxxxxxxx/payment_methods",
        )

    async def test_customer_taxid_retrieve(self, request_mock):
        await stripe.Customer.retrieve_tax_id(
            "cus_xxxxxxxxxxxxx", "txi_xxxxxxxxxxxxx"
        )
        request_mock.assert_requested(
            "get",
            "/v1/customers/cus_xxxxxxxxxxxxx/tax_ids/txi_xxxxxxxxxxxxx",
        )

    async def test_customer_search(self, request_mock):
        await stripe.Customer.search(
            query="name:'fakename' AND metadata['foo']:'bar'"
        )
        request_mock.assert_requested("get", "/v1/customers/search")

    async def test_customer_search2(self, request_mock):
        await stripe.Customer.search(
            query="name:'fakename' AND metadata['foo']:'bar'"
        )
        request_mock.assert_requested("get", "/v1/customers/search")

    async def test_dispute_list(self, request_mock):
        await stripe.Dispute.list(limit=3)
        request_mock.assert_requested("get", "/v1/disputes")

    async def test_dispute_retrieve(self, request_mock):
        await stripe.Dispute.retrieve("dp_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/disputes/dp_xxxxxxxxxxxxx")

    async def test_dispute_update(self, request_mock):
        await stripe.Dispute.modify(
            "dp_xxxxxxxxxxxxx", metadata={"order_id": "6735"}
        )
        request_mock.assert_requested("post", "/v1/disputes/dp_xxxxxxxxxxxxx")

    async def test_dispute_close(self, request_mock):
        await stripe.Dispute.close("dp_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post", "/v1/disputes/dp_xxxxxxxxxxxxx/close"
        )

    async def test_event_list(self, request_mock):
        await stripe.Event.list(limit=3)
        request_mock.assert_requested("get", "/v1/events")

    async def test_event_retrieve(self, request_mock):
        await stripe.Event.retrieve("evt_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/events/evt_xxxxxxxxxxxxx")

    async def test_filelink_list(self, request_mock):
        await stripe.FileLink.list(limit=3)
        request_mock.assert_requested("get", "/v1/file_links")

    async def test_filelink_create(self, request_mock):
        await stripe.FileLink.create(file="file_xxxxxxxxxxxxx")
        request_mock.assert_requested("post", "/v1/file_links")

    async def test_filelink_retrieve(self, request_mock):
        await stripe.FileLink.retrieve("link_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get", "/v1/file_links/link_xxxxxxxxxxxxx"
        )

    async def test_filelink_update(self, request_mock):
        await stripe.FileLink.modify(
            "link_xxxxxxxxxxxxx", metadata={"order_id": "6735"}
        )
        request_mock.assert_requested(
            "post", "/v1/file_links/link_xxxxxxxxxxxxx"
        )

    async def test_file_list(self, request_mock):
        await stripe.File.list(limit=3)
        request_mock.assert_requested("get", "/v1/files")

    async def test_file_retrieve(self, request_mock):
        await stripe.File.retrieve("file_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/files/file_xxxxxxxxxxxxx")

    async def test_financial_connections_account_list2(self, request_mock):
        await stripe.financial_connections.Account.list(
            account_holder={"customer": "cus_xxxxxxxxxxxxx"},
        )
        request_mock.assert_requested(
            "get", "/v1/financial_connections/accounts"
        )

    async def test_financial_connections_account_retrieve2(self, request_mock):
        await stripe.financial_connections.Account.retrieve("fca_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/financial_connections/accounts/fca_xxxxxxxxxxxxx",
        )

    async def test_financial_connections_account_list_owners2(self, request_mock):
        await stripe.financial_connections.Account.list_owners(
            "fca_xxxxxxxxxxxxx",
            limit=3,
            ownership="fcaowns_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "get",
            "/v1/financial_connections/accounts/fca_xxxxxxxxxxxxx/owners",
        )

    async def test_financial_connections_session_create2(self, request_mock):
        await stripe.financial_connections.Session.create(
            account_holder={
                "type": "customer",
                "customer": "cus_xxxxxxxxxxxxx",
            },
            permissions=["payment_method", "balances"],
            filters={"countries": ["US"]},
        )
        request_mock.assert_requested(
            "post", "/v1/financial_connections/sessions"
        )

    async def test_financial_connections_session_retrieve2(self, request_mock):
        await stripe.financial_connections.Session.retrieve("fcsess_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/financial_connections/sessions/fcsess_xxxxxxxxxxxxx",
        )

    async def test_identity_verificationreport_list(self, request_mock):
        await stripe.identity.VerificationReport.list(limit=3)
        request_mock.assert_requested(
            "get", "/v1/identity/verification_reports"
        )

    async def test_identity_verificationreport_retrieve(self, request_mock):
        await stripe.identity.VerificationReport.retrieve("vr_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/identity/verification_reports/vr_xxxxxxxxxxxxx",
        )

    async def test_identity_verificationsession_list(self, request_mock):
        await stripe.identity.VerificationSession.list(limit=3)
        request_mock.assert_requested(
            "get", "/v1/identity/verification_sessions"
        )

    async def test_identity_verificationsession_create(self, request_mock):
        await stripe.identity.VerificationSession.create(type="document")
        request_mock.assert_requested(
            "post", "/v1/identity/verification_sessions"
        )

    async def test_identity_verificationsession_retrieve(self, request_mock):
        await stripe.identity.VerificationSession.retrieve("vs_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/identity/verification_sessions/vs_xxxxxxxxxxxxx",
        )

    async def test_identity_verificationsession_update(self, request_mock):
        await stripe.identity.VerificationSession.modify(
            "vs_xxxxxxxxxxxxx",
            type="id_number",
        )
        request_mock.assert_requested(
            "post",
            "/v1/identity/verification_sessions/vs_xxxxxxxxxxxxx",
        )

    async def test_identity_verificationsession_cancel(self, request_mock):
        await stripe.identity.VerificationSession.cancel("vs_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/identity/verification_sessions/vs_xxxxxxxxxxxxx/cancel",
        )

    async def test_identity_verificationsession_redact(self, request_mock):
        await stripe.identity.VerificationSession.redact("vs_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/identity/verification_sessions/vs_xxxxxxxxxxxxx/redact",
        )

    async def test_invoiceitem_list(self, request_mock):
        await stripe.InvoiceItem.list(limit=3)
        request_mock.assert_requested("get", "/v1/invoiceitems")

    async def test_invoiceitem_create(self, request_mock):
        await stripe.InvoiceItem.create(
            customer="cus_xxxxxxxxxxxxx",
            price="price_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested("post", "/v1/invoiceitems")

    async def test_invoiceitem_delete(self, request_mock):
        await stripe.InvoiceItem.delete("ii_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete", "/v1/invoiceitems/ii_xxxxxxxxxxxxx"
        )

    async def test_invoiceitem_retrieve(self, request_mock):
        await stripe.InvoiceItem.retrieve("ii_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get", "/v1/invoiceitems/ii_xxxxxxxxxxxxx"
        )

    async def test_invoiceitem_update(self, request_mock):
        await stripe.InvoiceItem.modify(
            "ii_xxxxxxxxxxxxx", metadata={"order_id": "6735"}
        )
        request_mock.assert_requested(
            "post", "/v1/invoiceitems/ii_xxxxxxxxxxxxx"
        )

    async def test_invoice_list(self, request_mock):
        await stripe.Invoice.list(limit=3)
        request_mock.assert_requested("get", "/v1/invoices")

    async def test_invoice_create(self, request_mock):
        await stripe.Invoice.create(customer="cus_xxxxxxxxxxxxx")
        request_mock.assert_requested("post", "/v1/invoices")

    async def test_invoice_delete(self, request_mock):
        await stripe.Invoice.delete("in_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete", "/v1/invoices/in_xxxxxxxxxxxxx"
        )

    async def test_invoice_retrieve(self, request_mock):
        await stripe.Invoice.retrieve("in_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/invoices/in_xxxxxxxxxxxxx")

    async def test_invoice_update(self, request_mock):
        await stripe.Invoice.modify(
            "in_xxxxxxxxxxxxx", metadata={"order_id": "6735"}
        )
        request_mock.assert_requested("post", "/v1/invoices/in_xxxxxxxxxxxxx")

    async def test_invoice_finalize_invoice(self, request_mock):
        await stripe.Invoice.finalize_invoice("in_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/invoices/in_xxxxxxxxxxxxx/finalize",
        )

    async def test_invoice_mark_uncollectible(self, request_mock):
        await stripe.Invoice.mark_uncollectible("in_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/invoices/in_xxxxxxxxxxxxx/mark_uncollectible",
        )

    async def test_invoice_pay(self, request_mock):
        await stripe.Invoice.pay("in_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post", "/v1/invoices/in_xxxxxxxxxxxxx/pay"
        )

    async def test_invoice_send_invoice(self, request_mock):
        await stripe.Invoice.send_invoice("in_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post", "/v1/invoices/in_xxxxxxxxxxxxx/send"
        )

    async def test_invoice_void_invoice(self, request_mock):
        await stripe.Invoice.void_invoice("in_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post", "/v1/invoices/in_xxxxxxxxxxxxx/void"
        )

    async def test_invoice_search(self, request_mock):
        await stripe.Invoice.search(
            query="total>999 AND metadata['order_id']:'6735'"
        )
        request_mock.assert_requested("get", "/v1/invoices/search")

    async def test_issuing_authorization_list(self, request_mock):
        await stripe.issuing.Authorization.list(limit=3)
        request_mock.assert_requested("get", "/v1/issuing/authorizations")

    async def test_issuing_authorization_retrieve(self, request_mock):
        await stripe.issuing.Authorization.retrieve("iauth_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/issuing/authorizations/iauth_xxxxxxxxxxxxx",
        )

    async def test_issuing_authorization_update(self, request_mock):
        await stripe.issuing.Authorization.modify(
            "iauth_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/issuing/authorizations/iauth_xxxxxxxxxxxxx",
        )

    async def test_issuing_authorization_approve(self, request_mock):
        await stripe.issuing.Authorization.approve("iauth_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/issuing/authorizations/iauth_xxxxxxxxxxxxx/approve",
        )

    async def test_issuing_authorization_decline(self, request_mock):
        await stripe.issuing.Authorization.decline("iauth_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/issuing/authorizations/iauth_xxxxxxxxxxxxx/decline",
        )

    async def test_issuing_cardholder_list(self, request_mock):
        await stripe.issuing.Cardholder.list(limit=3)
        request_mock.assert_requested("get", "/v1/issuing/cardholders")

    async def test_issuing_cardholder_create(self, request_mock):
        await stripe.issuing.Cardholder.create(
            type="individual",
            name="Jenny Rosen",
            email="jenny.rosen@example.com",
            phone_number="+18888675309",
            billing={
                "address": {
                    "line1": "1234 Main Street",
                    "city": "San Francisco",
                    "state": "CA",
                    "country": "US",
                    "postal_code": "94111",
                },
            },
        )
        request_mock.assert_requested("post", "/v1/issuing/cardholders")

    async def test_issuing_cardholder_retrieve(self, request_mock):
        await stripe.issuing.Cardholder.retrieve("ich_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/issuing/cardholders/ich_xxxxxxxxxxxxx",
        )

    async def test_issuing_cardholder_update(self, request_mock):
        await stripe.issuing.Cardholder.modify(
            "ich_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/issuing/cardholders/ich_xxxxxxxxxxxxx",
        )

    async def test_issuing_card_list(self, request_mock):
        await stripe.issuing.Card.list(limit=3)
        request_mock.assert_requested("get", "/v1/issuing/cards")

    async def test_issuing_card_create(self, request_mock):
        await stripe.issuing.Card.create(
            cardholder="ich_xxxxxxxxxxxxx",
            currency="usd",
            type="virtual",
        )
        request_mock.assert_requested("post", "/v1/issuing/cards")

    async def test_issuing_card_retrieve(self, request_mock):
        await stripe.issuing.Card.retrieve("ic_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get", "/v1/issuing/cards/ic_xxxxxxxxxxxxx"
        )

    async def test_issuing_card_update(self, request_mock):
        await stripe.issuing.Card.modify(
            "ic_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post", "/v1/issuing/cards/ic_xxxxxxxxxxxxx"
        )

    async def test_issuing_dispute_list(self, request_mock):
        await stripe.issuing.Dispute.list(limit=3)
        request_mock.assert_requested("get", "/v1/issuing/disputes")

    async def test_issuing_dispute_create(self, request_mock):
        await stripe.issuing.Dispute.create(
            transaction="ipi_xxxxxxxxxxxxx",
            evidence={
                "reason": "fraudulent",
                "fraudulent": {"explanation": "Purchase was unrecognized."},
            },
        )
        request_mock.assert_requested("post", "/v1/issuing/disputes")

    async def test_issuing_dispute_retrieve(self, request_mock):
        await stripe.issuing.Dispute.retrieve("idp_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/issuing/disputes/idp_xxxxxxxxxxxxx",
        )

    async def test_issuing_dispute_submit(self, request_mock):
        await stripe.issuing.Dispute.submit("idp_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/issuing/disputes/idp_xxxxxxxxxxxxx/submit",
        )

    async def test_issuing_transaction_list(self, request_mock):
        await stripe.issuing.Transaction.list(limit=3)
        request_mock.assert_requested("get", "/v1/issuing/transactions")

    async def test_issuing_transaction_retrieve(self, request_mock):
        await stripe.issuing.Transaction.retrieve("ipi_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/issuing/transactions/ipi_xxxxxxxxxxxxx",
        )

    async def test_issuing_transaction_update(self, request_mock):
        await stripe.issuing.Transaction.modify(
            "ipi_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/issuing/transactions/ipi_xxxxxxxxxxxxx",
        )

    async def test_mandate_retrieve(self, request_mock):
        await stripe.Mandate.retrieve("mandate_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get", "/v1/mandates/mandate_xxxxxxxxxxxxx"
        )

    async def test_paymentintent_list(self, request_mock):
        await stripe.PaymentIntent.list(limit=3)
        request_mock.assert_requested("get", "/v1/payment_intents")

    async def test_paymentintent_create2(self, request_mock):
        await stripe.PaymentIntent.create(
            amount=2000,
            currency="usd",
            payment_method_types=["card"],
        )
        request_mock.assert_requested("post", "/v1/payment_intents")

    async def test_paymentintent_retrieve(self, request_mock):
        await stripe.PaymentIntent.retrieve("pi_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get", "/v1/payment_intents/pi_xxxxxxxxxxxxx"
        )

    async def test_paymentintent_update(self, request_mock):
        await stripe.PaymentIntent.modify(
            "pi_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents/pi_xxxxxxxxxxxxx",
        )

    async def test_paymentintent_apply_customer_balance(self, request_mock):
        await stripe.PaymentIntent.apply_customer_balance("pi_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents/pi_xxxxxxxxxxxxx/apply_customer_balance",
        )

    async def test_paymentintent_cancel(self, request_mock):
        await stripe.PaymentIntent.cancel("pi_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents/pi_xxxxxxxxxxxxx/cancel",
        )

    async def test_paymentintent_capture(self, request_mock):
        await stripe.PaymentIntent.capture("pi_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents/pi_xxxxxxxxxxxxx/capture",
        )

    async def test_paymentintent_confirm(self, request_mock):
        await stripe.PaymentIntent.confirm(
            "pi_xxxxxxxxxxxxx",
            payment_method="pm_card_visa",
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents/pi_xxxxxxxxxxxxx/confirm",
        )

    async def test_paymentintent_increment_authorization(self, request_mock):
        await stripe.PaymentIntent.increment_authorization(
            "pi_xxxxxxxxxxxxx",
            amount=2099,
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents/pi_xxxxxxxxxxxxx/increment_authorization",
        )

    async def test_paymentintent_search(self, request_mock):
        await stripe.PaymentIntent.search(
            query="status:'succeeded' AND metadata['order_id']:'6735'",
        )
        request_mock.assert_requested("get", "/v1/payment_intents/search")

    async def test_paymentlink_list(self, request_mock):
        await stripe.PaymentLink.list(limit=3)
        request_mock.assert_requested("get", "/v1/payment_links")

    async def test_paymentlink_create2(self, request_mock):
        await stripe.PaymentLink.create(
            line_items=[{"price": "price_xxxxxxxxxxxxx", "quantity": 1}],
        )
        request_mock.assert_requested("post", "/v1/payment_links")

    async def test_paymentlink_retrieve2(self, request_mock):
        await stripe.PaymentLink.retrieve("plink_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/payment_links/plink_xxxxxxxxxxxxx",
        )

    async def test_paymentlink_update(self, request_mock):
        await stripe.PaymentLink.modify("plink_xxxxxxxxxxxxx", active=False)
        request_mock.assert_requested(
            "post",
            "/v1/payment_links/plink_xxxxxxxxxxxxx",
        )

    async def test_paymentmethod_list(self, request_mock):
        await stripe.PaymentMethod.list(customer="cus_xxxxxxxxxxxxx", type="card")
        request_mock.assert_requested("get", "/v1/payment_methods")

    async def test_paymentmethod_create(self, request_mock):
        await stripe.PaymentMethod.create(
            type="card",
            card={
                "number": "4242424242424242",
                "exp_month": 5,
                "exp_year": 2023,
                "cvc": "314",
            },
        )
        request_mock.assert_requested("post", "/v1/payment_methods")

    async def test_paymentmethod_retrieve(self, request_mock):
        await stripe.PaymentMethod.retrieve("pm_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get", "/v1/payment_methods/pm_xxxxxxxxxxxxx"
        )

    async def test_paymentmethod_update(self, request_mock):
        await stripe.PaymentMethod.modify(
            "pm_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_methods/pm_xxxxxxxxxxxxx",
        )

    async def test_paymentmethod_attach(self, request_mock):
        await stripe.PaymentMethod.attach(
            "pm_xxxxxxxxxxxxx",
            customer="cus_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_methods/pm_xxxxxxxxxxxxx/attach",
        )

    async def test_paymentmethod_detach(self, request_mock):
        await stripe.PaymentMethod.detach("pm_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/payment_methods/pm_xxxxxxxxxxxxx/detach",
        )

    async def test_payout_list(self, request_mock):
        await stripe.Payout.list(limit=3)
        request_mock.assert_requested("get", "/v1/payouts")

    async def test_payout_create(self, request_mock):
        await stripe.Payout.create(amount=1100, currency="usd")
        request_mock.assert_requested("post", "/v1/payouts")

    async def test_payout_retrieve(self, request_mock):
        await stripe.Payout.retrieve("po_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/payouts/po_xxxxxxxxxxxxx")

    async def test_payout_update(self, request_mock):
        await stripe.Payout.modify("po_xxxxxxxxxxxxx", metadata={"order_id": "6735"})
        request_mock.assert_requested("post", "/v1/payouts/po_xxxxxxxxxxxxx")

    async def test_payout_cancel(self, request_mock):
        await stripe.Payout.cancel("po_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post", "/v1/payouts/po_xxxxxxxxxxxxx/cancel"
        )

    async def test_payout_reverse(self, request_mock):
        await stripe.Payout.reverse("po_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/payouts/po_xxxxxxxxxxxxx/reverse",
        )

    async def test_plan_list(self, request_mock):
        await stripe.Plan.list(limit=3)
        request_mock.assert_requested("get", "/v1/plans")

    async def test_plan_create(self, request_mock):
        await stripe.Plan.create(
            amount=2000,
            currency="usd",
            interval="month",
            product="prod_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested("post", "/v1/plans")

    async def test_plan_delete(self, request_mock):
        await stripe.Plan.delete("price_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete", "/v1/plans/price_xxxxxxxxxxxxx"
        )

    async def test_plan_retrieve(self, request_mock):
        await stripe.Plan.retrieve("price_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/plans/price_xxxxxxxxxxxxx")

    async def test_plan_update(self, request_mock):
        await stripe.Plan.modify(
            "price_xxxxxxxxxxxxx", metadata={"order_id": "6735"}
        )
        request_mock.assert_requested("post", "/v1/plans/price_xxxxxxxxxxxxx")

    async def test_price_list(self, request_mock):
        await stripe.Price.list(limit=3)
        request_mock.assert_requested("get", "/v1/prices")

    async def test_price_create2(self, request_mock):
        await stripe.Price.create(
            unit_amount=2000,
            currency="usd",
            recurring={"interval": "month"},
            product="prod_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested("post", "/v1/prices")

    async def test_price_retrieve(self, request_mock):
        await stripe.Price.retrieve("price_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/prices/price_xxxxxxxxxxxxx")

    async def test_price_update(self, request_mock):
        await stripe.Price.modify(
            "price_xxxxxxxxxxxxx", metadata={"order_id": "6735"}
        )
        request_mock.assert_requested("post", "/v1/prices/price_xxxxxxxxxxxxx")

    async def test_price_search(self, request_mock):
        await stripe.Price.search(
            query="active:'true' AND metadata['order_id']:'6735'"
        )
        request_mock.assert_requested("get", "/v1/prices/search")

    async def test_product_list(self, request_mock):
        await stripe.Product.list(limit=3)
        request_mock.assert_requested("get", "/v1/products")

    async def test_product_create(self, request_mock):
        await stripe.Product.create(name="Gold Special")
        request_mock.assert_requested("post", "/v1/products")

    async def test_product_delete(self, request_mock):
        await stripe.Product.delete("prod_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete", "/v1/products/prod_xxxxxxxxxxxxx"
        )

    async def test_product_retrieve(self, request_mock):
        await stripe.Product.retrieve("prod_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/products/prod_xxxxxxxxxxxxx")

    async def test_product_update(self, request_mock):
        await stripe.Product.modify(
            "prod_xxxxxxxxxxxxx", metadata={"order_id": "6735"}
        )
        request_mock.assert_requested(
            "post", "/v1/products/prod_xxxxxxxxxxxxx"
        )

    async def test_product_search(self, request_mock):
        await stripe.Product.search(
            query="active:'true' AND metadata['order_id']:'6735'"
        )
        request_mock.assert_requested("get", "/v1/products/search")

    async def test_promotioncode_list(self, request_mock):
        await stripe.PromotionCode.list(limit=3)
        request_mock.assert_requested("get", "/v1/promotion_codes")

    async def test_promotioncode_create(self, request_mock):
        await stripe.PromotionCode.create(coupon="Z4OV52SU")
        request_mock.assert_requested("post", "/v1/promotion_codes")

    async def test_promotioncode_retrieve(self, request_mock):
        await stripe.PromotionCode.retrieve("promo_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/promotion_codes/promo_xxxxxxxxxxxxx",
        )

    async def test_promotioncode_update(self, request_mock):
        await stripe.PromotionCode.modify(
            "promo_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/promotion_codes/promo_xxxxxxxxxxxxx",
        )

    async def test_quote_list(self, request_mock):
        await stripe.Quote.list(limit=3)
        request_mock.assert_requested("get", "/v1/quotes")

    async def test_quote_create(self, request_mock):
        await stripe.Quote.create(
            customer="cus_xxxxxxxxxxxxx",
            line_items=[{"price": "price_xxxxxxxxxxxxx", "quantity": 2}],
        )
        request_mock.assert_requested("post", "/v1/quotes")

    async def test_quote_retrieve(self, request_mock):
        await stripe.Quote.retrieve("qt_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/quotes/qt_xxxxxxxxxxxxx")

    async def test_quote_update(self, request_mock):
        await stripe.Quote.modify("qt_xxxxxxxxxxxxx", metadata={"order_id": "6735"})
        request_mock.assert_requested("post", "/v1/quotes/qt_xxxxxxxxxxxxx")

    async def test_quote_accept(self, request_mock):
        await stripe.Quote.accept("qt_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post", "/v1/quotes/qt_xxxxxxxxxxxxx/accept"
        )

    async def test_quote_cancel(self, request_mock):
        await stripe.Quote.cancel("qt_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post", "/v1/quotes/qt_xxxxxxxxxxxxx/cancel"
        )

    async def test_quote_finalize_quote(self, request_mock):
        await stripe.Quote.finalize_quote("qt_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/quotes/qt_xxxxxxxxxxxxx/finalize",
        )

    async def test_radar_earlyfraudwarning_list(self, request_mock):
        await stripe.radar.EarlyFraudWarning.list(limit=3)
        request_mock.assert_requested("get", "/v1/radar/early_fraud_warnings")

    async def test_radar_earlyfraudwarning_retrieve(self, request_mock):
        await stripe.radar.EarlyFraudWarning.retrieve("issfr_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/radar/early_fraud_warnings/issfr_xxxxxxxxxxxxx",
        )

    async def test_radar_valuelistitem_list(self, request_mock):
        await stripe.radar.ValueListItem.list(
            limit=3, value_list="rsl_xxxxxxxxxxxxx"
        )
        request_mock.assert_requested("get", "/v1/radar/value_list_items")

    async def test_radar_valuelistitem_create(self, request_mock):
        await stripe.radar.ValueListItem.create(
            value_list="rsl_xxxxxxxxxxxxx",
            value="1.2.3.4",
        )
        request_mock.assert_requested("post", "/v1/radar/value_list_items")

    async def test_radar_valuelistitem_delete(self, request_mock):
        await stripe.radar.ValueListItem.delete("rsli_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/radar/value_list_items/rsli_xxxxxxxxxxxxx",
        )

    async def test_radar_valuelistitem_retrieve(self, request_mock):
        await stripe.radar.ValueListItem.retrieve("rsli_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/radar/value_list_items/rsli_xxxxxxxxxxxxx",
        )

    async def test_radar_valuelist_list(self, request_mock):
        await stripe.radar.ValueList.list(limit=3)
        request_mock.assert_requested("get", "/v1/radar/value_lists")

    async def test_radar_valuelist_create(self, request_mock):
        await stripe.radar.ValueList.create(
            alias="custom_ip_xxxxxxxxxxxxx",
            name="Custom IP Blocklist",
            item_type="ip_address",
        )
        request_mock.assert_requested("post", "/v1/radar/value_lists")

    async def test_radar_valuelist_delete(self, request_mock):
        await stripe.radar.ValueList.delete("rsl_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/radar/value_lists/rsl_xxxxxxxxxxxxx",
        )

    async def test_radar_valuelist_retrieve(self, request_mock):
        await stripe.radar.ValueList.retrieve("rsl_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/radar/value_lists/rsl_xxxxxxxxxxxxx",
        )

    async def test_radar_valuelist_update(self, request_mock):
        await stripe.radar.ValueList.modify(
            "rsl_xxxxxxxxxxxxx",
            name="Updated IP Block List",
        )
        request_mock.assert_requested(
            "post",
            "/v1/radar/value_lists/rsl_xxxxxxxxxxxxx",
        )

    async def test_refund_list(self, request_mock):
        await stripe.Refund.list(limit=3)
        request_mock.assert_requested("get", "/v1/refunds")

    async def test_refund_create(self, request_mock):
        await stripe.Refund.create(charge="ch_xxxxxxxxxxxxx")
        request_mock.assert_requested("post", "/v1/refunds")

    async def test_refund_retrieve(self, request_mock):
        await stripe.Refund.retrieve("re_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/refunds/re_xxxxxxxxxxxxx")

    async def test_refund_update(self, request_mock):
        await stripe.Refund.modify("re_xxxxxxxxxxxxx", metadata={"order_id": "6735"})
        request_mock.assert_requested("post", "/v1/refunds/re_xxxxxxxxxxxxx")

    async def test_refund_cancel(self, request_mock):
        await stripe.Refund.cancel("re_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post", "/v1/refunds/re_xxxxxxxxxxxxx/cancel"
        )

    async def test_reporting_reportrun_list(self, request_mock):
        await stripe.reporting.ReportRun.list(limit=3)
        request_mock.assert_requested("get", "/v1/reporting/report_runs")

    async def test_reporting_reportrun_create(self, request_mock):
        await stripe.reporting.ReportRun.create(
            report_type="balance.summary.1",
            parameters={
                "interval_start": 1522540800,
                "interval_end": 1525132800,
            },
        )
        request_mock.assert_requested("post", "/v1/reporting/report_runs")

    async def test_reporting_reportrun_retrieve(self, request_mock):
        await stripe.reporting.ReportRun.retrieve("frr_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/reporting/report_runs/frr_xxxxxxxxxxxxx",
        )

    async def test_reporting_reporttype_list(self, request_mock):
        await stripe.reporting.ReportType.list()
        request_mock.assert_requested("get", "/v1/reporting/report_types")

    async def test_reporting_reporttype_retrieve(self, request_mock):
        await stripe.reporting.ReportType.retrieve("balance.summary.1")
        request_mock.assert_requested(
            "get",
            "/v1/reporting/report_types/balance.summary.1",
        )

    async def test_review_list(self, request_mock):
        await stripe.Review.list(limit=3)
        request_mock.assert_requested("get", "/v1/reviews")

    async def test_review_retrieve(self, request_mock):
        await stripe.Review.retrieve("prv_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/reviews/prv_xxxxxxxxxxxxx")

    async def test_review_approve(self, request_mock):
        await stripe.Review.approve("prv_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/reviews/prv_xxxxxxxxxxxxx/approve",
        )

    async def test_setupintent_list(self, request_mock):
        await stripe.SetupIntent.list(limit=3)
        request_mock.assert_requested("get", "/v1/setup_intents")

    async def test_setupintent_create(self, request_mock):
        await stripe.SetupIntent.create(payment_method_types=["card"])
        request_mock.assert_requested("post", "/v1/setup_intents")

    async def test_setupintent_retrieve(self, request_mock):
        await stripe.SetupIntent.retrieve("seti_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get", "/v1/setup_intents/seti_xxxxxxxxxxxxx"
        )

    async def test_setupintent_update(self, request_mock):
        await stripe.SetupIntent.modify(
            "seti_xxxxxxxxxxxxx",
            metadata={"user_id": "3435453"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/setup_intents/seti_xxxxxxxxxxxxx",
        )

    async def test_setupintent_cancel(self, request_mock):
        await stripe.SetupIntent.cancel("seti_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/setup_intents/seti_xxxxxxxxxxxxx/cancel",
        )

    async def test_setupintent_confirm(self, request_mock):
        await stripe.SetupIntent.confirm(
            "seti_xxxxxxxxxxxxx",
            payment_method="pm_card_visa",
        )
        request_mock.assert_requested(
            "post",
            "/v1/setup_intents/seti_xxxxxxxxxxxxx/confirm",
        )

    async def test_shippingrate_list2(self, request_mock):
        await stripe.ShippingRate.list(limit=3)
        request_mock.assert_requested("get", "/v1/shipping_rates")

    async def test_shippingrate_create2(self, request_mock):
        await stripe.ShippingRate.create(
            display_name="Ground shipping",
            type="fixed_amount",
            fixed_amount={"amount": 500, "currency": "usd"},
        )
        request_mock.assert_requested("post", "/v1/shipping_rates")

    async def test_shippingrate_retrieve(self, request_mock):
        await stripe.ShippingRate.retrieve("shr_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get", "/v1/shipping_rates/shr_xxxxxxxxxxxxx"
        )

    async def test_shippingrate_update(self, request_mock):
        await stripe.ShippingRate.modify(
            "shr_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/shipping_rates/shr_xxxxxxxxxxxxx",
        )

    async def test_sigma_scheduledqueryrun_list(self, request_mock):
        await stripe.sigma.ScheduledQueryRun.list(limit=3)
        request_mock.assert_requested("get", "/v1/sigma/scheduled_query_runs")

    async def test_sigma_scheduledqueryrun_retrieve(self, request_mock):
        await stripe.sigma.ScheduledQueryRun.retrieve("sqr_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/sigma/scheduled_query_runs/sqr_xxxxxxxxxxxxx",
        )

    async def test_source_retrieve(self, request_mock):
        await stripe.Source.retrieve("src_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/sources/src_xxxxxxxxxxxxx")

    async def test_source_retrieve2(self, request_mock):
        await stripe.Source.retrieve("src_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/sources/src_xxxxxxxxxxxxx")

    async def test_source_update(self, request_mock):
        await stripe.Source.modify(
            "src_xxxxxxxxxxxxx", metadata={"order_id": "6735"}
        )
        request_mock.assert_requested("post", "/v1/sources/src_xxxxxxxxxxxxx")

    async def test_subscriptionitem_list(self, request_mock):
        await stripe.SubscriptionItem.list(subscription="sub_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/subscription_items")

    async def test_subscriptionitem_create(self, request_mock):
        await stripe.SubscriptionItem.create(
            subscription="sub_xxxxxxxxxxxxx",
            price="price_xxxxxxxxxxxxx",
            quantity=2,
        )
        request_mock.assert_requested("post", "/v1/subscription_items")

    async def test_subscriptionitem_delete(self, request_mock):
        await stripe.SubscriptionItem.delete("si_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/subscription_items/si_xxxxxxxxxxxxx",
        )

    async def test_subscriptionitem_retrieve(self, request_mock):
        await stripe.SubscriptionItem.retrieve("si_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/subscription_items/si_xxxxxxxxxxxxx",
        )

    async def test_subscriptionitem_update(self, request_mock):
        await stripe.SubscriptionItem.modify(
            "si_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/subscription_items/si_xxxxxxxxxxxxx",
        )

    async def test_subscriptionschedule_list(self, request_mock):
        await stripe.SubscriptionSchedule.list(limit=3)
        request_mock.assert_requested("get", "/v1/subscription_schedules")

    async def test_subscriptionschedule_create(self, request_mock):
        await stripe.SubscriptionSchedule.create(
            customer="cus_xxxxxxxxxxxxx",
            start_date=1652909005,
            end_behavior="release",
            phases=[
                {
                    "items": [{"price": "price_xxxxxxxxxxxxx", "quantity": 1}],
                    "iterations": 12,
                },
            ],
        )
        request_mock.assert_requested("post", "/v1/subscription_schedules")

    async def test_subscriptionschedule_retrieve(self, request_mock):
        await stripe.SubscriptionSchedule.retrieve("sub_sched_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/subscription_schedules/sub_sched_xxxxxxxxxxxxx",
        )

    async def test_subscriptionschedule_update(self, request_mock):
        await stripe.SubscriptionSchedule.modify(
            "sub_sched_xxxxxxxxxxxxx",
            end_behavior="release",
        )
        request_mock.assert_requested(
            "post",
            "/v1/subscription_schedules/sub_sched_xxxxxxxxxxxxx",
        )

    async def test_subscriptionschedule_cancel(self, request_mock):
        await stripe.SubscriptionSchedule.cancel("sub_sched_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/subscription_schedules/sub_sched_xxxxxxxxxxxxx/cancel",
        )

    async def test_subscriptionschedule_release(self, request_mock):
        await stripe.SubscriptionSchedule.release("sub_sched_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/subscription_schedules/sub_sched_xxxxxxxxxxxxx/release",
        )

    async def test_subscription_list(self, request_mock):
        await stripe.Subscription.list(limit=3)
        request_mock.assert_requested("get", "/v1/subscriptions")

    async def test_subscription_create(self, request_mock):
        await stripe.Subscription.create(
            customer="cus_xxxxxxxxxxxxx",
            items=[{"price": "price_xxxxxxxxxxxxx"}],
        )
        request_mock.assert_requested("post", "/v1/subscriptions")

    async def test_subscription_retrieve(self, request_mock):
        await stripe.Subscription.retrieve("sub_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get", "/v1/subscriptions/sub_xxxxxxxxxxxxx"
        )

    async def test_subscription_update(self, request_mock):
        await stripe.Subscription.modify(
            "sub_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post", "/v1/subscriptions/sub_xxxxxxxxxxxxx"
        )

    async def test_subscription_search(self, request_mock):
        await stripe.Subscription.search(
            query="status:'active' AND metadata['order_id']:'6735'",
        )
        request_mock.assert_requested("get", "/v1/subscriptions/search")

    async def test_taxcode_list(self, request_mock):
        await stripe.TaxCode.list(limit=3)
        request_mock.assert_requested("get", "/v1/tax_codes")

    async def test_taxcode_retrieve(self, request_mock):
        await stripe.TaxCode.retrieve("txcd_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get", "/v1/tax_codes/txcd_xxxxxxxxxxxxx"
        )

    async def test_taxrate_list(self, request_mock):
        await stripe.TaxRate.list(limit=3)
        request_mock.assert_requested("get", "/v1/tax_rates")

    async def test_taxrate_create(self, request_mock):
        await stripe.TaxRate.create(
            display_name="VAT",
            description="VAT Germany",
            jurisdiction="DE",
            percentage=16,
            inclusive=False,
        )
        request_mock.assert_requested("post", "/v1/tax_rates")

    async def test_taxrate_retrieve(self, request_mock):
        await stripe.TaxRate.retrieve("txr_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/tax_rates/txr_xxxxxxxxxxxxx")

    async def test_taxrate_update(self, request_mock):
        await stripe.TaxRate.modify("txr_xxxxxxxxxxxxx", active=False)
        request_mock.assert_requested(
            "post", "/v1/tax_rates/txr_xxxxxxxxxxxxx"
        )

    async def test_terminal_configuration_list2(self, request_mock):
        await stripe.terminal.Configuration.list(limit=3)
        request_mock.assert_requested("get", "/v1/terminal/configurations")

    async def test_terminal_configuration_create2(self, request_mock):
        await stripe.terminal.Configuration.create(
            bbpos_wisepos_e={"splashscreen": "file_xxxxxxxxxxxxx"},
        )
        request_mock.assert_requested("post", "/v1/terminal/configurations")

    async def test_terminal_configuration_delete2(self, request_mock):
        await stripe.terminal.Configuration.delete("tmc_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/terminal/configurations/tmc_xxxxxxxxxxxxx",
        )

    async def test_terminal_configuration_retrieve2(self, request_mock):
        await stripe.terminal.Configuration.retrieve("tmc_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/terminal/configurations/tmc_xxxxxxxxxxxxx",
        )

    async def test_terminal_configuration_update2(self, request_mock):
        await stripe.terminal.Configuration.modify(
            "tmc_xxxxxxxxxxxxx",
            bbpos_wisepos_e={"splashscreen": "file_xxxxxxxxxxxxx"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/terminal/configurations/tmc_xxxxxxxxxxxxx",
        )

    async def test_terminal_connectiontoken_create(self, request_mock):
        await stripe.terminal.ConnectionToken.create()
        request_mock.assert_requested("post", "/v1/terminal/connection_tokens")

    async def test_terminal_location_list(self, request_mock):
        await stripe.terminal.Location.list(limit=3)
        request_mock.assert_requested("get", "/v1/terminal/locations")

    async def test_terminal_location_create(self, request_mock):
        await stripe.terminal.Location.create(
            display_name="My First Store",
            address={
                "line1": "1234 Main Street",
                "city": "San Francisco",
                "country": "US",
                "postal_code": "94111",
            },
        )
        request_mock.assert_requested("post", "/v1/terminal/locations")

    async def test_terminal_location_delete(self, request_mock):
        await stripe.terminal.Location.delete("tml_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/terminal/locations/tml_xxxxxxxxxxxxx",
        )

    async def test_terminal_location_retrieve(self, request_mock):
        await stripe.terminal.Location.retrieve("tml_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/terminal/locations/tml_xxxxxxxxxxxxx",
        )

    async def test_terminal_location_update(self, request_mock):
        await stripe.terminal.Location.modify(
            "tml_xxxxxxxxxxxxx",
            display_name="My First Store",
        )
        request_mock.assert_requested(
            "post",
            "/v1/terminal/locations/tml_xxxxxxxxxxxxx",
        )

    async def test_terminal_reader_list(self, request_mock):
        await stripe.terminal.Reader.list(limit=3)
        request_mock.assert_requested("get", "/v1/terminal/readers")

    async def test_terminal_reader_create(self, request_mock):
        await stripe.terminal.Reader.create(
            registration_code="puppies-plug-could",
            label="Blue Rabbit",
            location="tml_1234",
        )
        request_mock.assert_requested("post", "/v1/terminal/readers")

    async def test_terminal_reader_delete(self, request_mock):
        await stripe.terminal.Reader.delete("tmr_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/terminal/readers/tmr_xxxxxxxxxxxxx",
        )

    async def test_terminal_reader_retrieve(self, request_mock):
        await stripe.terminal.Reader.retrieve("tmr_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/terminal/readers/tmr_xxxxxxxxxxxxx",
        )

    async def test_terminal_reader_update(self, request_mock):
        await stripe.terminal.Reader.modify("tmr_xxxxxxxxxxxxx", label="Blue Rabbit")
        request_mock.assert_requested(
            "post",
            "/v1/terminal/readers/tmr_xxxxxxxxxxxxx",
        )

    async def test_terminal_reader_cancel_action(self, request_mock):
        await stripe.terminal.Reader.cancel_action("tmr_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/terminal/readers/tmr_xxxxxxxxxxxxx/cancel_action",
        )

    async def test_terminal_reader_process_payment_intent(self, request_mock):
        await stripe.terminal.Reader.process_payment_intent(
            "tmr_xxxxxxxxxxxxx",
            payment_intent="pi_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "post",
            "/v1/terminal/readers/tmr_xxxxxxxxxxxxx/process_payment_intent",
        )

    async def test_test_helpers_testclock_list2(self, request_mock):
        await stripe.test_helpers.TestClock.list(limit=3)
        request_mock.assert_requested("get", "/v1/test_helpers/test_clocks")

    async def test_test_helpers_testclock_create2(self, request_mock):
        await stripe.test_helpers.TestClock.create(frozen_time=1577836800)
        request_mock.assert_requested("post", "/v1/test_helpers/test_clocks")

    async def test_test_helpers_testclock_delete2(self, request_mock):
        await stripe.test_helpers.TestClock.delete("clock_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/test_helpers/test_clocks/clock_xxxxxxxxxxxxx",
        )

    async def test_test_helpers_testclock_retrieve2(self, request_mock):
        await stripe.test_helpers.TestClock.retrieve("clock_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/test_helpers/test_clocks/clock_xxxxxxxxxxxxx",
        )

    async def test_test_helpers_testclock_advance2(self, request_mock):
        await stripe.test_helpers.TestClock.advance(
            "clock_xxxxxxxxxxxxx",
            frozen_time=1652390605,
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/test_clocks/clock_xxxxxxxxxxxxx/advance",
        )

    async def test_token_create2(self, request_mock):
        await stripe.Token.create(
            bank_account={
                "country": "US",
                "currency": "usd",
                "account_holder_name": "Jenny Rosen",
                "account_holder_type": "individual",
                "routing_number": "110000000",
                "account_number": "000123456789",
            },
        )
        request_mock.assert_requested("post", "/v1/tokens")

    async def test_token_create3(self, request_mock):
        await stripe.Token.create(pii={"id_number": "000000000"})
        request_mock.assert_requested("post", "/v1/tokens")

    async def test_token_create4(self, request_mock):
        await stripe.Token.create(
            account={
                "individual": {"first_name": "Jane", "last_name": "Doe"},
                "tos_shown_and_accepted": True,
            },
        )
        request_mock.assert_requested("post", "/v1/tokens")

    async def test_token_create5(self, request_mock):
        await stripe.Token.create(
            person={
                "first_name": "Jane",
                "last_name": "Doe",
                "relationship": {"owner": True},
            },
        )
        request_mock.assert_requested("post", "/v1/tokens")

    async def test_token_create6(self, request_mock):
        await stripe.Token.create(cvc_update={"cvc": "123"})
        request_mock.assert_requested("post", "/v1/tokens")

    async def test_token_retrieve(self, request_mock):
        await stripe.Token.retrieve("tok_xxxx")
        request_mock.assert_requested("get", "/v1/tokens/tok_xxxx")

    async def test_topup_list(self, request_mock):
        await stripe.Topup.list(limit=3)
        request_mock.assert_requested("get", "/v1/topups")

    async def test_topup_create(self, request_mock):
        await stripe.Topup.create(
            amount=2000,
            currency="usd",
            description="Top-up for Jenny Rosen",
            statement_descriptor="Top-up",
        )
        request_mock.assert_requested("post", "/v1/topups")

    async def test_topup_retrieve(self, request_mock):
        await stripe.Topup.retrieve("tu_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/topups/tu_xxxxxxxxxxxxx")

    async def test_topup_update(self, request_mock):
        await stripe.Topup.modify("tu_xxxxxxxxxxxxx", metadata={"order_id": "6735"})
        request_mock.assert_requested("post", "/v1/topups/tu_xxxxxxxxxxxxx")

    async def test_topup_cancel(self, request_mock):
        await stripe.Topup.cancel("tu_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post", "/v1/topups/tu_xxxxxxxxxxxxx/cancel"
        )

    async def test_transfer_list(self, request_mock):
        await stripe.Transfer.list(limit=3)
        request_mock.assert_requested("get", "/v1/transfers")

    async def test_transfer_create(self, request_mock):
        await stripe.Transfer.create(
            amount=400,
            currency="usd",
            destination="acct_xxxxxxxxxxxxx",
            transfer_group="ORDER_95",
        )
        request_mock.assert_requested("post", "/v1/transfers")

    async def test_transfer_retrieve(self, request_mock):
        await stripe.Transfer.retrieve("tr_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/transfers/tr_xxxxxxxxxxxxx")

    async def test_transfer_update(self, request_mock):
        await stripe.Transfer.modify(
            "tr_xxxxxxxxxxxxx", metadata={"order_id": "6735"}
        )
        request_mock.assert_requested("post", "/v1/transfers/tr_xxxxxxxxxxxxx")

    async def test_transfer_transferreversal_retrieve(self, request_mock):
        await stripe.Transfer.retrieve_reversal(
            "tr_xxxxxxxxxxxxx", "trr_xxxxxxxxxxxxx"
        )
        request_mock.assert_requested(
            "get",
            "/v1/transfers/tr_xxxxxxxxxxxxx/reversals/trr_xxxxxxxxxxxxx",
        )

    async def test_transfer_transferreversal_update(self, request_mock):
        await stripe.Transfer.modify_reversal(
            "tr_xxxxxxxxxxxxx",
            "trr_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/transfers/tr_xxxxxxxxxxxxx/reversals/trr_xxxxxxxxxxxxx",
        )

    async def test_treasury_creditreversal_list(self, request_mock):
        await stripe.treasury.CreditReversal.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested("get", "/v1/treasury/credit_reversals")

    async def test_treasury_creditreversal_create(self, request_mock):
        await stripe.treasury.CreditReversal.create(
            received_credit="rc_xxxxxxxxxxxxx"
        )
        request_mock.assert_requested("post", "/v1/treasury/credit_reversals")

    async def test_treasury_creditreversal_retrieve(self, request_mock):
        await stripe.treasury.CreditReversal.retrieve("credrev_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/credit_reversals/credrev_xxxxxxxxxxxxx",
        )

    async def test_treasury_debitreversal_list(self, request_mock):
        await stripe.treasury.DebitReversal.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested("get", "/v1/treasury/debit_reversals")

    async def test_treasury_debitreversal_create(self, request_mock):
        await stripe.treasury.DebitReversal.create(received_debit="rd_xxxxxxxxxxxxx")
        request_mock.assert_requested("post", "/v1/treasury/debit_reversals")

    async def test_treasury_debitreversal_retrieve(self, request_mock):
        await stripe.treasury.DebitReversal.retrieve("debrev_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/debit_reversals/debrev_xxxxxxxxxxxxx",
        )

    async def test_treasury_financialaccount_list(self, request_mock):
        await stripe.treasury.FinancialAccount.list(limit=3)
        request_mock.assert_requested("get", "/v1/treasury/financial_accounts")

    async def test_treasury_financialaccount_create(self, request_mock):
        await stripe.treasury.FinancialAccount.create(
            supported_currencies=["usd"],
            features={},
        )
        request_mock.assert_requested(
            "post", "/v1/treasury/financial_accounts"
        )

    async def test_treasury_financialaccount_retrieve(self, request_mock):
        await stripe.treasury.FinancialAccount.retrieve("fa_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/financial_accounts/fa_xxxxxxxxxxxxx",
        )

    async def test_treasury_financialaccount_update(self, request_mock):
        await stripe.treasury.FinancialAccount.modify(
            "fa_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/treasury/financial_accounts/fa_xxxxxxxxxxxxx",
        )

    async def test_treasury_financialaccount_retrieve_features(self, request_mock):
        await stripe.treasury.FinancialAccount.retrieve_features("fa_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/financial_accounts/fa_xxxxxxxxxxxxx/features",
        )

    async def test_treasury_financialaccount_update_features(self, request_mock):
        await stripe.treasury.FinancialAccount.update_features(
            "fa_xxxxxxxxxxxxx",
            card_issuing={"requested": False},
        )
        request_mock.assert_requested(
            "post",
            "/v1/treasury/financial_accounts/fa_xxxxxxxxxxxxx/features",
        )

    async def test_treasury_inboundtransfer_list(self, request_mock):
        await stripe.treasury.InboundTransfer.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested("get", "/v1/treasury/inbound_transfers")

    async def test_treasury_inboundtransfer_create(self, request_mock):
        await stripe.treasury.InboundTransfer.create(
            financial_account="fa_xxxxxxxxxxxxx",
            amount=10000,
            currency="usd",
            origin_payment_method="pm_xxxxxxxxxxxxx",
            description="InboundTransfer from my bank account",
        )
        request_mock.assert_requested("post", "/v1/treasury/inbound_transfers")

    async def test_treasury_inboundtransfer_retrieve(self, request_mock):
        await stripe.treasury.InboundTransfer.retrieve("ibt_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/inbound_transfers/ibt_xxxxxxxxxxxxx",
        )

    async def test_treasury_inboundtransfer_cancel(self, request_mock):
        await stripe.treasury.InboundTransfer.cancel("ibt_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/treasury/inbound_transfers/ibt_xxxxxxxxxxxxx/cancel",
        )

    async def test_treasury_outboundpayment_list(self, request_mock):
        await stripe.treasury.OutboundPayment.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested("get", "/v1/treasury/outbound_payments")

    async def test_treasury_outboundpayment_create(self, request_mock):
        await stripe.treasury.OutboundPayment.create(
            financial_account="fa_xxxxxxxxxxxxx",
            amount=10000,
            currency="usd",
            customer="cu_xxxxxxxxxxxxx",
            destination_payment_method="pm_xxxxxxxxxxxxx",
            description="OutboundPayment to a 3rd party",
        )
        request_mock.assert_requested("post", "/v1/treasury/outbound_payments")

    async def test_treasury_outboundpayment_retrieve(self, request_mock):
        await stripe.treasury.OutboundPayment.retrieve("obp_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/outbound_payments/obp_xxxxxxxxxxxxx",
        )

    async def test_treasury_outboundpayment_cancel(self, request_mock):
        await stripe.treasury.OutboundPayment.cancel("obp_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/treasury/outbound_payments/obp_xxxxxxxxxxxxx/cancel",
        )

    async def test_treasury_outboundtransfer_list(self, request_mock):
        await stripe.treasury.OutboundTransfer.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested("get", "/v1/treasury/outbound_transfers")

    async def test_treasury_outboundtransfer_create(self, request_mock):
        await stripe.treasury.OutboundTransfer.create(
            financial_account="fa_xxxxxxxxxxxxx",
            destination_payment_method="pm_xxxxxxxxxxxxx",
            amount=500,
            currency="usd",
            description="OutboundTransfer to my external bank account",
        )
        request_mock.assert_requested(
            "post", "/v1/treasury/outbound_transfers"
        )

    async def test_treasury_outboundtransfer_retrieve(self, request_mock):
        await stripe.treasury.OutboundTransfer.retrieve("obt_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/outbound_transfers/obt_xxxxxxxxxxxxx",
        )

    async def test_treasury_outboundtransfer_cancel(self, request_mock):
        await stripe.treasury.OutboundTransfer.cancel("obt_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/treasury/outbound_transfers/obt_xxxxxxxxxxxxx/cancel",
        )

    async def test_treasury_receivedcredit_list(self, request_mock):
        await stripe.treasury.ReceivedCredit.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested("get", "/v1/treasury/received_credits")

    async def test_treasury_receivedcredit_retrieve(self, request_mock):
        await stripe.treasury.ReceivedCredit.retrieve("rc_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/received_credits/rc_xxxxxxxxxxxxx",
        )

    async def test_treasury_receiveddebit_list(self, request_mock):
        await stripe.treasury.ReceivedDebit.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested("get", "/v1/treasury/received_debits")

    async def test_treasury_receiveddebit_retrieve(self, request_mock):
        await stripe.treasury.ReceivedDebit.retrieve("rd_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/received_debits/rd_xxxxxxxxxxxxx",
        )

    async def test_treasury_transactionentry_list(self, request_mock):
        await stripe.treasury.TransactionEntry.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested(
            "get", "/v1/treasury/transaction_entries"
        )

    async def test_treasury_transactionentry_retrieve(self, request_mock):
        await stripe.treasury.TransactionEntry.retrieve("trxne_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/transaction_entries/trxne_xxxxxxxxxxxxx",
        )

    async def test_treasury_transaction_list(self, request_mock):
        await stripe.treasury.Transaction.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested("get", "/v1/treasury/transactions")

    async def test_treasury_transaction_retrieve(self, request_mock):
        await stripe.treasury.Transaction.retrieve("trxn_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/transactions/trxn_xxxxxxxxxxxxx",
        )

    async def test_webhookendpoint_list(self, request_mock):
        await stripe.WebhookEndpoint.list(limit=3)
        request_mock.assert_requested("get", "/v1/webhook_endpoints")

    async def test_webhookendpoint_create(self, request_mock):
        await stripe.WebhookEndpoint.create(
            url="https://example.com/my/webhook/endpoint",
            enabled_events=["charge.failed", "charge.succeeded"],
        )
        request_mock.assert_requested("post", "/v1/webhook_endpoints")

    async def test_webhookendpoint_delete(self, request_mock):
        await stripe.WebhookEndpoint.delete("we_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/webhook_endpoints/we_xxxxxxxxxxxxx",
        )

    async def test_webhookendpoint_retrieve(self, request_mock):
        await stripe.WebhookEndpoint.retrieve("we_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/webhook_endpoints/we_xxxxxxxxxxxxx",
        )

    async def test_webhookendpoint_update(self, request_mock):
        await stripe.WebhookEndpoint.modify(
            "we_xxxxxxxxxxxxx",
            url="https://example.com/new_endpoint",
        )
        request_mock.assert_requested(
            "post",
            "/v1/webhook_endpoints/we_xxxxxxxxxxxxx",
        )
