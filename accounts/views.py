from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .forms import RegisterForm, LoginForm


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = LoginForm


def logout_view(request):
    logout(request)
    return redirect('home')