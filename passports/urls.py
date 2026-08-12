from django.urls import path
from . import views

urlpatterns = [
    path('applications/', views.passport_application_list_view, name='passport_application_list'),
    path('applications/<int:application_id>/', views.passport_application_detail_view, name='passport_application_detail'),
    path('applications/create/', views.passport_application_create_view, name='passport_application_create'),
    path('applications/<int:application_id>/review/', views.passport_review_action_view, name='passport_review_action'),
]
