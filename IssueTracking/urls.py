"""IssueTracking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from django.contrib.auth import views as auth_views
from myProfile import views as profile_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        "",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login"
    ),
    path("main/", views.index, name="main"),
    path('profile', profile_views.index, name="profile"),
    path('api/change_password', profile_views.change_password, name="change_password"),
    path("logout/", views.logout_view, name="logout"),
    path('api/logout',views.api_logout,name="api_logout")
]
