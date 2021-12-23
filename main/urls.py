from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:project_id>/', views.index_with_project, name='index_with_project'),
    path('project_creating/', views.project_creating, name='project_creating'),
    path('<int:project_id>/project_editing/', views.project_editing, name='project_editing'),
]
