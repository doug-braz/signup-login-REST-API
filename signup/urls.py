from django.urls import path
from .views import SignUp, RegistrationView

urlpatterns = [
    path('', SignUp, name='SignUp'),
    path('register/', RegistrationView, name='Registration'),
]