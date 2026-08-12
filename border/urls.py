from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.border_checkpoint_dashboard_view, name='border_checkpoint_dashboard'),
    path('log/', views.border_log_entry_view, name='border_log_entry'),
]
