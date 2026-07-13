from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('products/', include('apps.products.urls')),
    path('categories/', include('apps.categories.urls')),
    path('suppliers/', include('apps.suppliers.urls')),
    path('customers/', include('apps.customers.urls')),
    path('inventory/', include('apps.inventory.urls')),
    path('purchase-orders/', include('apps.purchase_orders.urls')),
    path('sales/', include('apps.sales.urls')),
    path('reports/', include('apps.reports.urls')),
    path('users/', include('apps.users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
