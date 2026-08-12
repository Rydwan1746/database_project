from django.urls import path
from . import views

urlpatterns = [
    path('history/', views.travel_history_search_view, name='travel_history_search'),
    path('report/', views.travel_report_export_view, name='travel_report_export'),
]
