from django.urls import path
from . import views


app_name = 'payment'

urlpatterns = [
    path('', views.ItemListView.as_view()),
    path('buy/<int:id>/', views.BuyItem.as_view(), name='buy'),
    path('item/<int:id>/', views.ItemDetailView.as_view(), name='item'),
    path('create/', views.CreateOrderView.as_view(), name='create_order'),
    path('detail/<int:id>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('buy_order/<int:id>/', views.BuyOrder.as_view(), name='buy_order'),
]
