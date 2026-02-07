from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post_list/', views.post_list, name='post_list'),
    path('post_list/post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('post_create/', views.post_create, name='post_create'),
    path('post_edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('post_delete/<int:pk>/', views.post_delete, name='post_delete'),
]