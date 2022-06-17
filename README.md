# async-stripe

[![Build Status](https://github.com/bhch/async-stripe/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/bhch/async-stripe/actions/workflows/ci.yml)

An asynchronous wrapper around Stripe's official python library. 

## How it works

async-stripe monkey-patches the stripe library and replaces the synchronous 
http request methods with asynchronous methods.

Monkey-patching allows us to avoid a complete rewrite and keep the usage api 
similar to the official library.

This **doesn't use threads**, but **actual async coroutines** and 
[non-blocking http client][1] to make requests. Hence, the performance is much
better than other wrapper libraries which use threading.

## Install

Install requires Python 3.6 or newer.

```sh
$ pip install async-stripe
```

## Usage

The usage api is similar to Stripe's official library:

```python
from async_stripe import stripe

stripe.api_key = '<stripe-secret-key>'

payment_intent = await stripe.PaymentIntent.create(amount=1000, currency='usd')

print(payment_intent.id)
```

---

**/!\ Note:** Since this library monkey-patches the actual `stripe` library, 
you should avoid using the two in the same process.

Once you import `async_stripe`, the official `stripe` library gets patched with 
async methods and the original synchronous api won't be available.

---

## Configuration

Please see [`stripe-python`'s README][5] file for configuring logging and other things.

#### Unsupported configurations:

`async-stripe` aims to be a drop-in async replacement for `stripe`. However, 
there are a few things which are not yet supported:

 - Custom http client: Currently, it's not possible to configure a 
 custom http client and Tornado's [`AsyncHTTPClient`][1] will be used by default.
 - Proxy: Connecting to api via a proxy is not supported yet.

## Development and Testing

When adding new features and monkey-patches, please add relevant tests and 
ensure that all the tests also pass. 

In most cases, you shouldn't need to write the tests yourself: you can just 
copy-paste the tests form the original stripe library and change the synchronous 
methods to asynchronous methods. 

For testing, first, [install and run the `stripe-mock` api server][2].

Next, install `pytest`, `pytest-mock` and `pytest-asyncio` python packages in 
your virtualenv.

Finally, run the tests like this:

```sh
$ pytest tests

# or run a specific test
$ pytest tests/api_resources/test_customer.py
$ pytest tests/api_resources/test_customer.py::TestCustomer
```

## License

A lot of the code (especially tests) are copied with slight modifications from 
Stripe's official library. That code is licensed under 
[MIT License][3].

Rest of the original code is licensed under [BSD-3-Clause License][4].


[1]: https://www.tornadoweb.org/en/stable/httpclient.html#tornado.httpclient.AsyncHTTPClient
[2]: https://github.com/stripe/stripe-mock
[3]: LICENSE.stripe.txt
[4]: LICENSE.txt
[5]: https://github.com/stripe/stripe-python/blob/master/README.md