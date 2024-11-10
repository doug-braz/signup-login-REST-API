from django.urls import path
from .views import LoginView

urlpatterns = [
    path('', LoginView, name='login'),
    #path('loginAPI/', LoginView.as_view(), name='LoginView'),
]