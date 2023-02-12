import stripe
import os
from dotenv import load_dotenv
load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def create_stripe_checkout_session(item):
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                    'description': item.description
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
    )
    return session.id