from django.shortcuts import render, redirect
from account.models import Account
from django.views import View
from account.forms import RegisterUserForm
from django.contrib.auth import authenticate, login, logout

class RegisterView(View):
    def get(self, request):
        return render(request, 'registration/register.html', {'form':RegisterUserForm()})

    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            form.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')
        form = RegisterUserForm()

class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login-view')

