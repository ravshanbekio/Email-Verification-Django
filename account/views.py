from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from account.forms import RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from account.models import Account

class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'registration/register.html', {'form':RegisterUserForm()})

    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            form.save()
            domain_name = get_current_site(request).domain
            template = render_to_string('email_template.html',{'name':request.user.username, 'link':f'http://www.{domain_name}/account/verify/{username}/'})
            email = EmailMessage(
                'Welcome!',
                template,
                settings.EMAIL_HOST_USER,
                [form.cleaned_data['email']],
            )
            email.fail_silently=False
            email.send()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return redirect('register-view')

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

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login-view')

class VerifyView(View):
    def get(self, request, user):
        result = Account.objects.filter(username=user)
        if result:
            return HttpResponse('Email verified')
        return HttpResponse('Email not verified')
