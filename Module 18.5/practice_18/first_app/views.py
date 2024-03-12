from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib import messages
from .forms import RegisterForm, ChangeUserData


def home(request):
    return render(request, './homepage.html')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account Created successfully')
                form.save()
                return redirect('login')
        else:
            form = RegisterForm()
        return render(request, './signup.html', {'form': form})
    else:
        return redirect('profile')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=name, password=userpass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged In Successfully')
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, './login.html', {'form': form})
    else:
        messages.success(request, 'You are already Logged In')
        return redirect('profile')


def profile(request):
    if request.user.is_authenticated:
        return render(request, './profile.html')
    else:
        return redirect('login')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('homepage')


def changepass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password Updated Successfully')
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, './changepass.html', {'form': form})
    else:
        return redirect('login')


def changepassold(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password Updated Successfully')
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, './changepass.html', {'form': form})
    else:
        return redirect('login')


