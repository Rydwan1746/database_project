from django.urls import path
from . import views

urlpatterns = [
    path('queue/', views.visa_queue_view, name='visa_queue'),
    path('<int:visa_id>/', views.visa_detail_view, name='visa_detail'),
    path('<int:visa_id>/process/', views.visa_process_view, name='visa_process'),
]
