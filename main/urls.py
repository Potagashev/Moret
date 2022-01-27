from django.urls import path

from main import views
from main.views import SignUpUser, LoginUser, logout_user

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:project_id>/', views.index_with_project, name='index_with_project'),
    path('project_creating/', views.project_creating, name='project_creating'),
    path('<int:project_id>/project_editing/', views.project_editing, name='project_editing'),
    path('login/', LoginUser.as_view(), name='login'),
    path('sign_up/', SignUpUser.as_view(), name='sign_up'),
    path('logout/', logout_user, name='logout'),
]
