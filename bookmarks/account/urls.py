from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # our custom login view
    # path("login/", views.user_login, name="login"),
    # Django's built-in login view
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", views.dashboard, name="dashboard"),
]
