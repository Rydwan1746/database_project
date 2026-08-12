from django.urls import path
from . import views

urlpatterns = [
    path('', views.citizen_list_view, name='citizen_list'),
    path('<int:citizen_id>/', views.citizen_detail_view, name='citizen_detail'),
    path('create/', views.citizen_create_view, name='citizen_create'),
    path('<int:citizen_id>/update/', views.citizen_update_view, name='citizen_update'),
]
