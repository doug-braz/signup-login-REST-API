from django.urls import path
from .views import SignUp, CreateAccountView

urlpatterns = [
    path('', SignUp, name='SignUp'),
    path('createaccountAPI/', CreateAccountView.as_view(), name='CreateAccount'),
]