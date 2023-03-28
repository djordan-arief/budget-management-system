from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def create_new_account(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login-page')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/new_account.html', {'form': form})


def logoutView(request):
    logout(request)
    messages.success(request, "Log out successfully")
    return redirect('login-page')


def loginView(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                username = form.cleaned_data.get('username')
                messages.success(request, f'Welcome {username}')
                return redirect('expenses')
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('login-page')
    else:
        form = LoginForm()
    return render(request, 'authentication/login.html', {'form': form})
