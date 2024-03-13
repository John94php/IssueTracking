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
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from myProfile import views as profile_views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path(
        "",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login"
    ),
    path("main/", views.index, name="main"),
    path('profile', profile_views.index, name="profile"),
    path('api/change_password', profile_views.change_password, name="change_password"),
    path('change_language/<str:language_code>/', profile_views.change_language, name="change_language"),
    path("logout/", views.logout_view, name="logout"),
    path('api/logout', views.api_logout, name="api_logout"),
    path('api/user_notifications',profile_views.user_notifications, name="user_notifications")
)
urlpatterns += [
    path("i18n/", include("django.conf.urls.i18n"))
]