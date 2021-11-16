from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('main/', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.index_with_project, name='index_with_project')
]
