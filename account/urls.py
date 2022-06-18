from django.urls import path
from account.views import RegisterView, LoginView, LogoutView, VerifyView

urlpatterns = [
    path('register/',RegisterView.as_view(), name='register-view'),
    path('login/',LoginView.as_view(), name='login-view'),
    path('logout/',LogoutView.as_view(), name='logout-view'),
    path('verify/<user>/',VerifyView.as_view(), name='verify-email'),
]