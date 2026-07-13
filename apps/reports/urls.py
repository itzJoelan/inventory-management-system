from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('', views.reports_list, name='list'),
    path('inventory/', views.inventory_report, name='inventory'),
    path('sales/', views.sales_report, name='sales'),
    path('purchase/', views.purchase_report, name='purchase'),
]
