from django.http import JsonResponse

from payment.services import create_stripe_checkout_session

from .models import Item


def buy_item(request, id):
    item = Item.objects.get(id=id)
    session_id = create_stripe_checkout_session(item)
    return JsonResponse({"session_id": session_id})
