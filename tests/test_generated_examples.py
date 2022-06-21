from __future__ import absolute_import, division, print_function

import pytest
import stripe


pytestmark = pytest.mark.asyncio


class TestGeneratedExamples:
    async def test_apps_secret_create(self, request_mock):
        await stripe.apps.Secret.create(
            name="sec_123",
            payload="very secret string",
            scope={"type": "account"},
        )
        request_mock.assert_requested("post", "/v1/apps/secrets")

    async def test_apps_secret_find(self, request_mock):
        await stripe.apps.Secret.find(name="sec_123", scope={"type": "account"})
        request_mock.assert_requested("get", "/v1/apps/secrets/find")

    async def test_apps_secret_delete_where(self, request_mock):
        await stripe.apps.Secret.delete_where(
            name="sec_123", scope={"type": "account"}
        )
        request_mock.assert_requested("post", "/v1/apps/secrets/delete")

    async def test_customer_list_payment_methods(self, request_mock):
        await stripe.Customer.list_payment_methods("cus_xyz", type="card")
        request_mock.assert_requested(
            "get",
            "/v1/customers/cus_xyz/payment_methods",
        )

    async def test_checkout_session_expire(self, request_mock):
        await stripe.checkout.Session.expire("sess_xyz")
        request_mock.assert_requested(
            "post",
            "/v1/checkout/sessions/sess_xyz/expire",
        )

    async def test_shippingrate_create(self, request_mock):
        await stripe.ShippingRate.create(
            display_name="Sample Shipper",
            fixed_amount={"currency": "usd", "amount": 400},
            type="fixed_amount",
        )
        request_mock.assert_requested("post", "/v1/shipping_rates")

    async def test_shippingrate_list(self, request_mock):
        await stripe.ShippingRate.list()
        request_mock.assert_requested("get", "/v1/shipping_rates")

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

    async def test_paymentintent_create(self, request_mock):
        await stripe.PaymentIntent.create(
            amount=1099,
            currency="eur",
            automatic_payment_methods={"enabled": True},
        )
        request_mock.assert_requested("post", "/v1/payment_intents")

    async def test_paymentlink_create(self, request_mock):
        await stripe.PaymentLink.create(
            line_items=[{"price": "price_xxxxxxxxxxxxx", "quantity": 1}],
        )
        request_mock.assert_requested("post", "/v1/payment_links")

    async def test_paymentlink_list_line_items(self, request_mock):
        await stripe.PaymentLink.list_line_items("pl_xyz")
        request_mock.assert_requested(
            "get", "/v1/payment_links/pl_xyz/line_items"
        )

    async def test_paymentlink_retrieve(self, request_mock):
        await stripe.PaymentLink.retrieve("pl_xyz")
        request_mock.assert_requested("get", "/v1/payment_links/pl_xyz")

    async def test_paymentintent_verify_microdeposits(self, request_mock):
        await stripe.PaymentIntent.verify_microdeposits("pi_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents/pi_xxxxxxxxxxxxx/verify_microdeposits",
        )

    async def test_setupintent_verify_microdeposits(self, request_mock):
        await stripe.SetupIntent.verify_microdeposits("seti_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/setup_intents/seti_xxxxxxxxxxxxx/verify_microdeposits",
        )

    async def test_test_helpers_testclock_create(self, request_mock):
        await stripe.test_helpers.TestClock.create(frozen_time=123, name="cogsworth")
        request_mock.assert_requested("post", "/v1/test_helpers/test_clocks")

    async def test_test_helpers_testclock_retrieve(self, request_mock):
        await stripe.test_helpers.TestClock.retrieve("clock_xyz")
        request_mock.assert_requested(
            "get",
            "/v1/test_helpers/test_clocks/clock_xyz",
        )

    async def test_test_helpers_testclock_list(self, request_mock):
        await stripe.test_helpers.TestClock.list()
        request_mock.assert_requested("get", "/v1/test_helpers/test_clocks")

    async def test_test_helpers_testclock_delete(self, request_mock):
        await stripe.test_helpers.TestClock.delete("clock_xyz")
        request_mock.assert_requested(
            "delete",
            "/v1/test_helpers/test_clocks/clock_xyz",
        )

    async def test_test_helpers_testclock_advance(self, request_mock):
        await stripe.test_helpers.TestClock.advance("clock_xyz", frozen_time=142)
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/test_clocks/clock_xyz/advance",
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

    async def test_terminal_configuration_list(self, request_mock):
        await stripe.terminal.Configuration.list()
        request_mock.assert_requested("get", "/v1/terminal/configurations")

    async def test_terminal_configuration_retrieve(self, request_mock):
        await stripe.terminal.Configuration.retrieve("uc_123")
        request_mock.assert_requested(
            "get", "/v1/terminal/configurations/uc_123"
        )

    async def test_terminal_configuration_create(self, request_mock):
        await stripe.terminal.Configuration.create()
        request_mock.assert_requested("post", "/v1/terminal/configurations")

    async def test_terminal_configuration_update(self, request_mock):
        await stripe.terminal.Configuration.modify(
            "uc_123",
            tipping={"usd": {"fixed_amounts": [10]}},
        )
        request_mock.assert_requested(
            "post", "/v1/terminal/configurations/uc_123"
        )

    async def test_terminal_configuration_delete(self, request_mock):
        await stripe.terminal.Configuration.delete("uc_123")
        request_mock.assert_requested(
            "delete",
            "/v1/terminal/configurations/uc_123",
        )

    async def test_refund_expire(self, request_mock):
        await stripe.Refund.TestHelpers.expire("re_123")
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/refunds/re_123/expire",
        )

    async def test_order_create(self, request_mock):
        await stripe.Order.create(
            description="description",
            currency="usd",
            line_items=[{"description": "my line item"}],
        )
        request_mock.assert_requested("post", "/v1/orders")

    async def test_order_update(self, request_mock):
        await stripe.Order.modify("order_xyz")
        request_mock.assert_requested("post", "/v1/orders/order_xyz")

    async def test_order_list_line_items(self, request_mock):
        await stripe.Order.list_line_items("order_xyz")
        request_mock.assert_requested("get", "/v1/orders/order_xyz/line_items")

    async def test_order_cancel(self, request_mock):
        await stripe.Order.cancel("order_xyz")
        request_mock.assert_requested("post", "/v1/orders/order_xyz/cancel")

    async def test_order_reopen(self, request_mock):
        await stripe.Order.reopen("order_xyz")
        request_mock.assert_requested("post", "/v1/orders/order_xyz/reopen")

    async def test_order_submit(self, request_mock):
        await stripe.Order.submit("order_xyz", expected_total=100)
        request_mock.assert_requested("post", "/v1/orders/order_xyz/submit")

    async def test_order_update2(self, request_mock):
        await stripe.Order.modify("order_xyz")
        request_mock.assert_requested("post", "/v1/orders/order_xyz")

    async def test_financial_connections_account_retrieve(self, request_mock):
        await stripe.financial_connections.Account.retrieve("fca_xyz")
        request_mock.assert_requested(
            "get",
            "/v1/financial_connections/accounts/fca_xyz",
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

    async def test_financial_connections_account_disconnect(self, request_mock):
        await stripe.financial_connections.Account.disconnect("fca_xyz")
        request_mock.assert_requested(
            "post",
            "/v1/financial_connections/accounts/fca_xyz/disconnect",
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

    async def test_financial_connections_account_list(self, request_mock):
        await stripe.financial_connections.Account.list()
        request_mock.assert_requested(
            "get", "/v1/financial_connections/accounts"
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

    async def test_treasury_outboundtransfer_post(self, request_mock):
        await stripe.treasury.OutboundTransfer.TestHelpers.post("obt_123")
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/treasury/outbound_transfers/obt_123/post",
        )

    async def test_treasury_outboundtransfer_fail(self, request_mock):
        await stripe.treasury.OutboundTransfer.TestHelpers.fail("obt_123")
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/treasury/outbound_transfers/obt_123/fail",
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

    async def test_customer_list(self, request_mock):
        await stripe.Customer.list(limit=3)
        request_mock.assert_requested("get", "/v1/customers")

    async def test_customer_search(self, request_mock):
        await stripe.Customer.search(
            query="name:'fakename' AND metadata['foo']:'bar'"
        )
        request_mock.assert_requested("get", "/v1/customers/search")

    async def test_charge_search(self, request_mock):
        await stripe.Charge.search(
            query="amount>999 AND metadata['order_id']:'6735'"
        )
        request_mock.assert_requested("get", "/v1/charges/search")

    async def test_customer_search2(self, request_mock):
        await stripe.Customer.search(
            query="name:'fakename' AND metadata['foo']:'bar'"
        )
        request_mock.assert_requested("get", "/v1/customers/search")

    async def test_paymentintent_create2(self, request_mock):
        await stripe.PaymentIntent.create(
            amount=2000,
            currency="usd",
            payment_method_types=["card"],
        )
        request_mock.assert_requested("post", "/v1/payment_intents")

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

    async def test_paymentintent_apply_customer_balance(self, request_mock):
        await stripe.PaymentIntent.apply_customer_balance("pi_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents/pi_xxxxxxxxxxxxx/apply_customer_balance",
        )

    async def test_setupattempt_list(self, request_mock):
        await stripe.SetupAttempt.list(limit=3, setup_intent="si_xyz")
        request_mock.assert_requested("get", "/v1/setup_attempts")

    async def test_refund_cancel(self, request_mock):
        await stripe.Refund.cancel("re_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post", "/v1/refunds/re_xxxxxxxxxxxxx/cancel"
        )

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

    async def test_paymentmethod_list(self, request_mock):
        await stripe.PaymentMethod.list(customer="cus_xxxxxxxxxxxxx", type="card")
        request_mock.assert_requested("get", "/v1/payment_methods")

    async def test_customer_list_payment_methods2(self, request_mock):
        await stripe.Customer.list_payment_methods("cus_xxxxxxxxxxxxx", type="card")
        request_mock.assert_requested(
            "get",
            "/v1/customers/cus_xxxxxxxxxxxxx/payment_methods",
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

    async def test_source_retrieve(self, request_mock):
        await stripe.Source.retrieve("src_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/sources/src_xxxxxxxxxxxxx")

    async def test_source_update(self, request_mock):
        await stripe.Source.modify(
            "src_xxxxxxxxxxxxx", metadata={"order_id": "6735"}
        )
        request_mock.assert_requested("post", "/v1/sources/src_xxxxxxxxxxxxx")

    async def test_product_create(self, request_mock):
        await stripe.Product.create(name="Gold Special")
        request_mock.assert_requested("post", "/v1/products")

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

    async def test_product_list(self, request_mock):
        await stripe.Product.list(limit=3)
        request_mock.assert_requested("get", "/v1/products")

    async def test_product_delete(self, request_mock):
        await stripe.Product.delete("prod_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete", "/v1/products/prod_xxxxxxxxxxxxx"
        )

    async def test_product_search(self, request_mock):
        await stripe.Product.search(
            query="active:'true' AND metadata['order_id']:'6735'"
        )
        request_mock.assert_requested("get", "/v1/products/search")

    async def test_price_create(self, request_mock):
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

    async def test_price_list(self, request_mock):
        await stripe.Price.list(limit=3)
        request_mock.assert_requested("get", "/v1/prices")

    async def test_price_search(self, request_mock):
        await stripe.Price.search(
            query="active:'true' AND metadata['order_id']:'6735'"
        )
        request_mock.assert_requested("get", "/v1/prices/search")

    async def test_coupon_create(self, request_mock):
        await stripe.Coupon.create(
            percent_off=25.5,
            duration="repeating",
            duration_in_months=3,
        )
        request_mock.assert_requested("post", "/v1/coupons")

    async def test_coupon_retrieve(self, request_mock):
        await stripe.Coupon.retrieve("Z4OV52SU")
        request_mock.assert_requested("get", "/v1/coupons/Z4OV52SU")

    async def test_coupon_update(self, request_mock):
        await stripe.Coupon.modify("Z4OV52SU", metadata={"order_id": "6735"})
        request_mock.assert_requested("post", "/v1/coupons/Z4OV52SU")

    async def test_coupon_delete(self, request_mock):
        await stripe.Coupon.delete("Z4OV52SU")
        request_mock.assert_requested("delete", "/v1/coupons/Z4OV52SU")

    async def test_coupon_list(self, request_mock):
        await stripe.Coupon.list(limit=3)
        request_mock.assert_requested("get", "/v1/coupons")

    async def test_promotioncode_create(self, request_mock):
        await stripe.PromotionCode.create(coupon="Z4OV52SU")
        request_mock.assert_requested("post", "/v1/promotion_codes")

    async def test_promotioncode_update(self, request_mock):
        await stripe.PromotionCode.modify(
            "promo_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/promotion_codes/promo_xxxxxxxxxxxxx",
        )

    async def test_promotioncode_retrieve(self, request_mock):
        await stripe.PromotionCode.retrieve("promo_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/promotion_codes/promo_xxxxxxxxxxxxx",
        )

    async def test_promotioncode_list(self, request_mock):
        await stripe.PromotionCode.list(limit=3)
        request_mock.assert_requested("get", "/v1/promotion_codes")

    async def test_taxcode_list(self, request_mock):
        await stripe.TaxCode.list(limit=3)
        request_mock.assert_requested("get", "/v1/tax_codes")

    async def test_taxcode_retrieve(self, request_mock):
        await stripe.TaxCode.retrieve("txcd_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get", "/v1/tax_codes/txcd_xxxxxxxxxxxxx"
        )

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

    async def test_taxrate_list(self, request_mock):
        await stripe.TaxRate.list(limit=3)
        request_mock.assert_requested("get", "/v1/tax_rates")

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

    async def test_shippingrate_list2(self, request_mock):
        await stripe.ShippingRate.list(limit=3)
        request_mock.assert_requested("get", "/v1/shipping_rates")

    async def test_checkout_session_create2(self, request_mock):
        await stripe.checkout.Session.create(
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
            line_items=[{"price": "price_xxxxxxxxxxxxx", "quantity": 2}],
            mode="payment",
        )
        request_mock.assert_requested("post", "/v1/checkout/sessions")

    async def test_checkout_session_expire2(self, request_mock):
        await stripe.checkout.Session.expire("cs_test_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/checkout/sessions/cs_test_xxxxxxxxxxxxx/expire",
        )

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

    async def test_paymentlink_list(self, request_mock):
        await stripe.PaymentLink.list(limit=3)
        request_mock.assert_requested("get", "/v1/payment_links")

    async def test_invoice_search(self, request_mock):
        await stripe.Invoice.search(
            query="total>999 AND metadata['order_id']:'6735'"
        )
        request_mock.assert_requested("get", "/v1/invoices/search")

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

    async def test_quote_finalize_quote(self, request_mock):
        await stripe.Quote.finalize_quote("qt_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/quotes/qt_xxxxxxxxxxxxx/finalize",
        )

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

    async def test_quote_list(self, request_mock):
        await stripe.Quote.list(limit=3)
        request_mock.assert_requested("get", "/v1/quotes")

    async def test_subscription_search(self, request_mock):
        await stripe.Subscription.search(
            query="status:'active' AND metadata['order_id']:'6735'",
        )
        request_mock.assert_requested("get", "/v1/subscriptions/search")

    async def test_test_helpers_testclock_create2(self, request_mock):
        await stripe.test_helpers.TestClock.create(frozen_time=1577836800)
        request_mock.assert_requested("post", "/v1/test_helpers/test_clocks")

    async def test_test_helpers_testclock_retrieve2(self, request_mock):
        await stripe.test_helpers.TestClock.retrieve("clock_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/test_helpers/test_clocks/clock_xxxxxxxxxxxxx",
        )

    async def test_test_helpers_testclock_delete2(self, request_mock):
        await stripe.test_helpers.TestClock.delete("clock_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
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

    async def test_test_helpers_testclock_list2(self, request_mock):
        await stripe.test_helpers.TestClock.list(limit=3)
        request_mock.assert_requested("get", "/v1/test_helpers/test_clocks")

    async def test_terminal_reader_create(self, request_mock):
        await stripe.terminal.Reader.create(
            registration_code="puppies-plug-could",
            label="Blue Rabbit",
            location="tml_1234",
        )
        request_mock.assert_requested("post", "/v1/terminal/readers")

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

    async def test_terminal_reader_delete(self, request_mock):
        await stripe.terminal.Reader.delete("tmr_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/terminal/readers/tmr_xxxxxxxxxxxxx",
        )

    async def test_terminal_reader_list(self, request_mock):
        await stripe.terminal.Reader.list(limit=3)
        request_mock.assert_requested("get", "/v1/terminal/readers")

    async def test_terminal_reader_process_payment_intent(self, request_mock):
        await stripe.terminal.Reader.process_payment_intent(
            "tmr_xxxxxxxxxxxxx",
            payment_intent="pi_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "post",
            "/v1/terminal/readers/tmr_xxxxxxxxxxxxx/process_payment_intent",
        )

    async def test_terminal_reader_process_setup_intent(self, request_mock):
        await stripe.terminal.Reader.process_setup_intent(
            "tmr_xxxxxxxxxxxxx",
            setup_intent="seti_xxxxxxxxxxxxx",
            customer_consent_collected=True,
        )
        request_mock.assert_requested(
            "post",
            "/v1/terminal/readers/tmr_xxxxxxxxxxxxx/process_setup_intent",
        )

    async def test_terminal_reader_cancel_action(self, request_mock):
        await stripe.terminal.Reader.cancel_action("tmr_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/terminal/readers/tmr_xxxxxxxxxxxxx/cancel_action",
        )

    async def test_terminal_configuration_create2(self, request_mock):
        await stripe.terminal.Configuration.create(
            bbpos_wisepos_e={"splashscreen": "file_xxxxxxxxxxxxx"},
        )
        request_mock.assert_requested("post", "/v1/terminal/configurations")

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

    async def test_terminal_configuration_delete2(self, request_mock):
        await stripe.terminal.Configuration.delete("tmc_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/terminal/configurations/tmc_xxxxxxxxxxxxx",
        )

    async def test_terminal_configuration_list2(self, request_mock):
        await stripe.terminal.Configuration.list(limit=3)
        request_mock.assert_requested("get", "/v1/terminal/configurations")

    async def test_treasury_financialaccount_create(self, request_mock):
        await stripe.treasury.FinancialAccount.create(
            supported_currencies=["usd"],
            features={},
        )
        request_mock.assert_requested(
            "post", "/v1/treasury/financial_accounts"
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

    async def test_treasury_financialaccount_retrieve(self, request_mock):
        await stripe.treasury.FinancialAccount.retrieve("fa_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/financial_accounts/fa_xxxxxxxxxxxxx",
        )

    async def test_treasury_financialaccount_list(self, request_mock):
        await stripe.treasury.FinancialAccount.list(limit=3)
        request_mock.assert_requested("get", "/v1/treasury/financial_accounts")

    async def test_treasury_financialaccount_update_features(self, request_mock):
        await stripe.treasury.FinancialAccount.update_features("fa_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/treasury/financial_accounts/fa_xxxxxxxxxxxxx/features",
        )

    async def test_treasury_financialaccount_retrieve_features(self, request_mock):
        await stripe.treasury.FinancialAccount.retrieve_features("fa_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/financial_accounts/fa_xxxxxxxxxxxxx/features",
        )

    async def test_treasury_transaction_retrieve(self, request_mock):
        await stripe.treasury.Transaction.retrieve("trxn_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/transactions/trxn_xxxxxxxxxxxxx",
        )

    async def test_treasury_transaction_list(self, request_mock):
        await stripe.treasury.Transaction.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested("get", "/v1/treasury/transactions")

    async def test_treasury_transactionentry_retrieve(self, request_mock):
        await stripe.treasury.TransactionEntry.retrieve("trxne_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/transaction_entries/trxne_xxxxxxxxxxxxx",
        )

    async def test_treasury_transactionentry_list(self, request_mock):
        await stripe.treasury.TransactionEntry.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested(
            "get", "/v1/treasury/transaction_entries"
        )

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

    async def test_treasury_outboundtransfer_cancel(self, request_mock):
        await stripe.treasury.OutboundTransfer.cancel("obt_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/treasury/outbound_transfers/obt_xxxxxxxxxxxxx/cancel",
        )

    async def test_treasury_outboundtransfer_retrieve(self, request_mock):
        await stripe.treasury.OutboundTransfer.retrieve("obt_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/outbound_transfers/obt_xxxxxxxxxxxxx",
        )

    async def test_treasury_outboundtransfer_list(self, request_mock):
        await stripe.treasury.OutboundTransfer.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested("get", "/v1/treasury/outbound_transfers")

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

    async def test_treasury_outboundpayment_cancel(self, request_mock):
        await stripe.treasury.OutboundPayment.cancel("obp_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/treasury/outbound_payments/obp_xxxxxxxxxxxxx/cancel",
        )

    async def test_treasury_outboundpayment_retrieve(self, request_mock):
        await stripe.treasury.OutboundPayment.retrieve("obp_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/outbound_payments/obp_xxxxxxxxxxxxx",
        )

    async def test_treasury_outboundpayment_list(self, request_mock):
        await stripe.treasury.OutboundPayment.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested("get", "/v1/treasury/outbound_payments")

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

    async def test_treasury_inboundtransfer_list(self, request_mock):
        await stripe.treasury.InboundTransfer.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested("get", "/v1/treasury/inbound_transfers")

    async def test_treasury_inboundtransfer_cancel(self, request_mock):
        await stripe.treasury.InboundTransfer.cancel("ibt_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/treasury/inbound_transfers/ibt_xxxxxxxxxxxxx/cancel",
        )

    async def test_treasury_receivedcredit_retrieve(self, request_mock):
        await stripe.treasury.ReceivedCredit.retrieve("rc_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/received_credits/rc_xxxxxxxxxxxxx",
        )

    async def test_treasury_receivedcredit_list(self, request_mock):
        await stripe.treasury.ReceivedCredit.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested("get", "/v1/treasury/received_credits")

    async def test_treasury_receiveddebit_retrieve(self, request_mock):
        await stripe.treasury.ReceivedDebit.retrieve("rd_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/received_debits/rd_xxxxxxxxxxxxx",
        )

    async def test_treasury_receiveddebit_list(self, request_mock):
        await stripe.treasury.ReceivedDebit.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested("get", "/v1/treasury/received_debits")

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

    async def test_treasury_creditreversal_list(self, request_mock):
        await stripe.treasury.CreditReversal.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested("get", "/v1/treasury/credit_reversals")

    async def test_treasury_debitreversal_create(self, request_mock):
        await stripe.treasury.DebitReversal.create(received_debit="rd_xxxxxxxxxxxxx")
        request_mock.assert_requested("post", "/v1/treasury/debit_reversals")

    async def test_treasury_debitreversal_retrieve(self, request_mock):
        await stripe.treasury.DebitReversal.retrieve("debrev_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/debit_reversals/debrev_xxxxxxxxxxxxx",
        )

    async def test_treasury_debitreversal_list(self, request_mock):
        await stripe.treasury.DebitReversal.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested("get", "/v1/treasury/debit_reversals")

    async def test_financial_connections_account_retrieve2(self, request_mock):
        await stripe.financial_connections.Account.retrieve("fca_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/financial_connections/accounts/fca_xxxxxxxxxxxxx",
        )

    async def test_financial_connections_account_list2(self, request_mock):
        await stripe.financial_connections.Account.list(
            account_holder={"customer": "cus_xxxxxxxxxxxxx"},
        )
        request_mock.assert_requested(
            "get", "/v1/financial_connections/accounts"
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

    async def test_source_retrieve2(self, request_mock):
        await stripe.Source.retrieve("src_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/sources/src_xxxxxxxxxxxxx")

    async def test_identity_verificationsession_create(self, request_mock):
        await stripe.identity.VerificationSession.create(type="document")
        request_mock.assert_requested(
            "post", "/v1/identity/verification_sessions"
        )

    async def test_identity_verificationsession_list(self, request_mock):
        await stripe.identity.VerificationSession.list(limit=3)
        request_mock.assert_requested(
            "get", "/v1/identity/verification_sessions"
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

    async def test_identity_verificationreport_retrieve(self, request_mock):
        await stripe.identity.VerificationReport.retrieve("vr_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/identity/verification_reports/vr_xxxxxxxxxxxxx",
        )

    async def test_identity_verificationreport_list(self, request_mock):
        await stripe.identity.VerificationReport.list(limit=3)
        request_mock.assert_requested(
            "get", "/v1/identity/verification_reports"
        )

    async def test_webhookendpoint_create(self, request_mock):
        await stripe.WebhookEndpoint.create(
            url="https://example.com/my/webhook/endpoint",
            enabled_events=["charge.failed", "charge.succeeded"],
        )
        request_mock.assert_requested("post", "/v1/webhook_endpoints")

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

    async def test_webhookendpoint_list(self, request_mock):
        await stripe.WebhookEndpoint.list(limit=3)
        request_mock.assert_requested("get", "/v1/webhook_endpoints")

    async def test_webhookendpoint_delete(self, request_mock):
        await stripe.WebhookEndpoint.delete("we_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/webhook_endpoints/we_xxxxxxxxxxxxx",
        )
