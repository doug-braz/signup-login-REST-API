from django.urls import path
from .views import homepage, members_index
urlpatterns = [
    path('', homepage, name='home'),
    path('members_index/', members_index, name='members_index')
]