from django.urls import path
from .views import Login, CreateAccountView

urlpatterns = [
    path('', Login, name='Login'),
    path('loginAPI/', LoginView.as_view(), name='LoginView'),
]