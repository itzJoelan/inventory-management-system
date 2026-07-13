from django.urls import path
from . import views

app_name = 'purchase_orders'

urlpatterns = [
    path('', views.purchase_order_list, name='list'),
    path('create/', views.purchase_order_create, name='create'),
    path('<int:pk>/', views.purchase_order_detail, name='detail'),
    path('<int:pk>/receive/', views.receive_inventory, name='receive'),
]
