from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.inventory_list, name='list'),
    path('stock-in/', views.stock_in, name='stock_in'),
    path('stock-out/', views.stock_out, name='stock_out'),
    path('adjustment/', views.stock_adjustment, name='adjustment'),
    path('history/', views.inventory_history, name='history'),
]
