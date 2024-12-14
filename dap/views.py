from django.shortcuts import render, redirect
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views import View
from .forms import CreateUser
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy


def home(request):
    return render(request, "dap/index.html")


class SignUp(View):
    def get(self, request):
        form = CreateUser()
        return render(request, "dap/register.html", {"form": form})

    def post(self, request):
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

        return render(request, "dap/register.html", {"form": form})


class Login(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "dap/login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")

        return render(request, "dap/login.html", {"form": form})


class ResetPass(PasswordResetView):
    template_name = "dap/reset_pass.html"
    email_template_name = "dap/reset_pass_email.html"
    subject_template_name = "dap/reset_pass_subject.txt"
    success_url = reverse_lazy("login")
    success_message = (
        "We've emailed you instructions for setting your password, "
        "if an account exists with the email you entered. You should receive them shortly."
        "If you don't receive an email, please make sure you've entered the address you registered with, "
        "and check your spam folder."
    )


@login_required
class ChangePass(View):
    def get(self, request):
        form = PasswordChangeForm()
        return render(request, "dap/change_pass.html", {"form": form})

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("profile")

        return render(request, "dap/change_pass.html", {"form": form})


@login_required
def dashboard(request):
    user = request.user
    return render(request, "dap/dashboard.html", {"user": user})


@login_required
def profile(request):
    user = request.user
    return render(request, "dap/profile.html", {"user": user})
