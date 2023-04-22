"""Groupify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('groups/<int:group_id>/', views.get_group_by_id, name='get_group_by_id'),
    path('groups/<int:group_id>/remove-user/', views.remove_user_from_group, name='remove_user_from_group'),
    path('groups/', views.get_all_groups, name='get_all_groups'),
    path('group/<int:group_id>/add-user/', views.add_user_to_group, name='add_user_to_group'),
    path('group/<int:group_id>/update/', views.update_group, name='update_group'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', admin.site.urls),
]

