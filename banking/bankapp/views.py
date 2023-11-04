from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import ApplicationForm, SignupForm
from .models import User_Table
from .models import Application
from django.contrib.auth import authenticate
from django.db.utils import IntegrityError

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm  # Import the LoginForm you created






def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or any other page
                return redirect('bankapp:apply')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})






def home(request):
    return render(request, 'home.html')




def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('bankapp:login')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

def apply(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bankapp:msg')
    else:
        form = ApplicationForm()

    return render(request, 'apply.html', {'form': form})



def success(request):
    return render(request, 'application_success.html')

def user_logout(request):
    logout(request)
    return redirect('bankapp:home')
