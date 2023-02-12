import stripe
import os
from dotenv import load_dotenv
load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
def create_line_item(item):
    return {
        'price_data': {
            'currency': 'usd',
            'product_data': {
                'name': item.name,
                'description': item.description
            },
            'unit_amount': item.price,
        },
        'quantity': 1,
    }

def create_stripe_checkout_session(item=None, order=None):
    line_items = []
    if item:
        line_items = [create_line_item(item)]
    elif order:
        for item in order.items.all():
            line_items.append(create_line_item(item))

    session = stripe.checkout.Session.create(
        line_items=line_items,
        mode='payment',
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
    )
    return session.id
