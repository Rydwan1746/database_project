from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.officer_login_view, name='officer_login'),
    path('logout/', views.officer_logout_view, name='officer_logout'),
    path('manage/', views.officer_management_list_view, name='officer_management_list'),
]
