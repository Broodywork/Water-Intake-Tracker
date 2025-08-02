from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_page, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add/', views.add_intake, name='add_intake'),
    path('list/', views.intake_list, name='intake_list'),
    path('edit/<int:id>/', views.edit_intake, name='edit_intake'),
    path('delete/<int:id>/', views.delete_intake, name='delete_intake'),
    path('compare/', views.compare_intake, name='compare_intake'),
]


