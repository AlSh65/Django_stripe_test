import os

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from payment.services import create_stripe_checkout_session

from .models import Item



class BuyItem(View):
    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, id=kwargs['id'])
        session_id = create_stripe_checkout_session(item)
        return JsonResponse({"session_id": session_id})


class ItemDetail(View):
    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, id=kwargs['id'])
        stripe_key = os.getenv("STRIPE_PUBLIC_KEY")
        return render(request, 'item_detail.html', {'item': item, 'stripe_key' : stripe_key})
