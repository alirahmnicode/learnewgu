from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserLoginForm, UserRegisterForm


def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                    cd["username"], cd["email"], cd["password"])
            login(request, user)
            message = "your account created succesfully"
            messages.add_message(request, messages.SUCCESS, message)
            return redirect('/')
        else:
            messages.warning(request, 'somthing is warng')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = UserRegisterForm()
        return render(request, 'user/signup.html', {'form':form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                message = "you are loggined succesfully"
                messages.add_message(request, messages.SUCCESS, message)
                return redirect('core:dashboard')
            else:
                message = 'Username or password is wrong!'
                messages.add_message(request, messages.ERROR, message)
                return redirect('user:login')
        else:
            messages.warning(request, 'somthing is warng')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = UserLoginForm()
        return render(request, 'user/login.html', {'form':form})



def logout_view(request):
    logout(request)
    return redirect('/')