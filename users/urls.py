"""Defines URL patterns for users"""

from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = "users"
urlpatterns = [
    # Login page
    path("", views.LoginView.as_view(), name="login"),

    path("sign_up/", views.sign_up, name="sign_up"),

    # Logout page
    path("log_out/", views.log_out, name="log_out"),
]