from django.shortcuts import render, redirect
from .forms import SignUpForm, EditAccountForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def signup(response):
    if response.method == "POST":
        form = SignUpForm(response.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(response, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(response,'signup.html', {"form": form})


def change_password(response):
    if response.method == "POST":
        form = PasswordChangeForm(data=response.POST, user=response.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(response, form.user)
            return redirect('/accounts/account')
        else:
            return redirect('/accounts/account/change_password')
    else:
        form = PasswordChangeForm(user=response.user)
    return render(response, 'change_password.html',{"form": form})

def own_account(request):
    return render(request,'account.html')


def edit_account(response):
    if response.method == "POST":
        form = EditAccountForm(response.POST, instance=response.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/account')
    else:
        form = EditAccountForm(instance=response.user)
    return render(response, 'edit_account.html',{"form": form})
