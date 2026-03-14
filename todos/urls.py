from django.urls import path
from . import views

urlpatterns = [
    # Regular HTML pages
    path('', views.todo_list, name='todo_list'),
    path('add/', views.todo_add, name='todo_add'),
    path('complete/<int:pk>/', views.todo_complete, name='todo_complete'),
    path('edit/<int:pk>/', views.todo_edit, name='todo_edit'),
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),
    path('register/', views.register, name='register'),
    path('category_add/', views.category_add, name='category_add'),
    # API endpoints for React
    path('api/', views.api_todo_list, name='api_todo_list'),
    path('api/<int:pk>/', views.api_todo_detail, name='api_todo_detail'),
]