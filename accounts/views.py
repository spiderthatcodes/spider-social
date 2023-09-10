from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm, PasswordUpdateForm, SignUpForm, UserEditForm, DetailForm


# sign up
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        details = DetailForm(request.POST)
        if form.is_valid() and details.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_confirmation = form.cleaned_data['password_confirmation']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            if password == password_confirmation:
                user = User.objects.create_user(
                    username,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )
                details.instance.spider = user
                details.save()

                login(request, user)

                return redirect('home')
            else:
                form.add_error("password", "Passwords don't match")

    else:
        form = SignUpForm()
        details = DetailForm()

    context = {
        "form": form,
        "details": details
    }

    return render(request, "accounts/signup.html", context)


# edit user - requires auth


# edit password - requires auth


# login
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(
                request,
                username=username,
                password=password
                )

            if user is not None:
                login(request, user)
                return redirect('home')

    else:
        form = LoginForm()

    context = {
        "form": form
    }

    return render(request, "accounts/login.html", context)


# logout
def user_logout(request):
    logout(request)
    return redirect('login')

import random
@login_required(login_url='/accounts/login/')
def account_home(request):
    current_user = request.user
    users = User.objects.exclude(id=current_user.id)

    random_index = random.randint(0,len(users)-1)
    context = {
        "user": current_user,
        "users": users,
        "highlight": users[random_index]
    }
    return render(request, "accounts/home.html", context)
