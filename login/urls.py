from django.urls import path
from .views import LoginView, Login

urlpatterns = [
    path('', Login, name='login'),
    path('loginAPI/', LoginView.as_view(), name='api-login'),
]