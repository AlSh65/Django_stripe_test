from django.urls import path
from .views import buy_item

urlpatterns = [
    path('buy/<int:id>/', buy_item),
]
