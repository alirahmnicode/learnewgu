from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm


class UserRegisterView(View):
    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        return render(request, 'register/signup.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                username=cd['username'], email=cd['email'], password=cd['password1'])
            login(request, user)
            messages.success(
                request, 'your account is created and you are logged in')
            return redirect('/')