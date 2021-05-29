# async-stripe

An asynchronous wrapper around the official stripe library. 

/!\ **Note:** This is still a work in progress and doesn't provide async support 
for all the resources yet.

## Usage

The usage api is kept very similar to stripe's official library:

```python
from async_stripe import stripe

stripe.api_key = '<stripe-secret-key>'

payment_intent = await stripe.PaymentIntent.create(amount=1000, currency='usd')

print(payment_intent.id)
```

### Sync usage

Currently, only a limited operations have async usage. For those cases, you'll 
have to fall back to using sync code (without the `await` keyword).

## Requirements

 + Tornado (used for making async http requests)
 + stripe (official stripe library)


## License

[BSD-3-Clause](LICENSE.txt)