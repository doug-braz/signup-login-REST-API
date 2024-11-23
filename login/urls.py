from django.urls import path
from .views import LoginView, Login, Logout

urlpatterns = [
    path('', Login, name='login'),
    path('loginAPI/', LoginView.as_view(), name='api-login'),
    path('logout/', Logout, name='logout')
]