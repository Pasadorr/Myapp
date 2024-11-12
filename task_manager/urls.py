# task_manager/urls.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import home, add_task, delete_task, complete_task, register, user_login, user_logout

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_task, name='add_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('complete/<int:task_id>/', complete_task, name='complete_task'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view, name='logout'),
]