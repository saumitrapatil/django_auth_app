from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetConfirmView,
    PasswordChangeView,
)
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup", views.SignUp.as_view(), name="signup"),
    path("login", views.Login.as_view(), name="login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("profile", views.profile, name="profile"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("reset-password", views.ResetPass.as_view(), name="reset-password"),
    path(
        "password-confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="dap/password_confirm.html",
            success_url=reverse_lazy("login"),
        ),
        name="password_confirm",
    ),
    path(
        "change-password",
        PasswordChangeView.as_view(
            template_name="dap/change_pass.html", success_url=reverse_lazy("profile")
        ),
        name="change-password",
    ),
]
