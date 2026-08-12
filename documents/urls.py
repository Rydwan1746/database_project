from django.urls import path
from . import views

urlpatterns = [
    path('queue/', views.document_verification_queue_view, name='document_verification_queue'),
    path('<int:document_id>/verify/', views.document_verify_action_view, name='document_verify_action'),
]
