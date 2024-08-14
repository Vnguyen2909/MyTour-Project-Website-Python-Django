from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import RegisterUserForm, UpdateUserForm, UpdateAdminUserForm
from django.contrib.auth.decorators import login_required, user_passes_test


def is_superuser_or_staff(user):
    """Example test function checking for superuser or staff"""
    return user.is_superuser or user.is_staff


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("natours:index")
        else:
            messages.success(request, ("There Was An Error Logging In, Try Again..."))
            return redirect("members:login")
    else:
        return render(request, "authenticate/login.html")


def logout_user(request):
    logout(request)
    # messages.success(request, ("You Were Logged Out!"))
    return redirect("natours:index")


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect("natours:index")
    else:
        form = RegisterUserForm()
    return render(
        request,
        "authenticate/register_user.html",
        {
            "form": form,
        },
    )


def edit_profile(request):
    user = request.user
    form = UpdateUserForm(request.POST or None, request.FILES or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, "info_user.html", {"user": user, "form": form})


@login_required(login_url="/members/login_user")
def all_user(request):
    data = {"users": User.objects.all()}
    return render(request, "all_user.html", data)
    # data = {"users": User.objects.all()}
    # return render(request, "all_user.html", data)


def update_user(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.user.is_superuser:
        form = UpdateAdminUserForm(
            request.POST or None, request.FILES or None, instance=user
        )
    else:
        form = UpdateUserForm(
            request.POST or None, request.FILES or None, instance=user
        )

    if form.is_valid():
        form.save()
        return redirect("members:all-user")
    return render(request, "info_user.html", {"user": user, "form": form})
