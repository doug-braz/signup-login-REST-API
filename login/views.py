from django.shortcuts import render

def LoginView(request):
    return render(request, 'login/login.html')


# Create your views here.
