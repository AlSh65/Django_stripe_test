from django.urls import path
from .views import BuyItem, ItemDetail


app_name = 'payment'

urlpatterns = [
    path('buy/<int:id>/', BuyItem.as_view(), name='buy'),
    path('item/<int:id>/', ItemDetail.as_view()),
]
