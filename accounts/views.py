from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserSignupForm, UserLoginForm


def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])  
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')  
    else:
        form = UserSignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('welcome') 
                
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})
def welcome_view(request):
    return render(request, 'accounts/welcome.html')