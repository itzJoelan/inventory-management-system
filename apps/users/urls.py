from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.user_list, name='list'),
    path('profile/', views.user_profile, name='profile'),
    path('<int:pk>/edit/', views.user_edit, name='edit'),
]
