import stripe
import os
from dotenv import load_dotenv
load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def create_stripe_payment(object):
    if hasattr(object, 'total_price'):
        amount = int(object.total_price() * 100)
    elif hasattr(object, 'price'):
        amount = object.price
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=object.currency,
        payment_method_types=["card"]
    )
    return intent.client_secret