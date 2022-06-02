from django.shortcuts import render
from account.models import Account
from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')