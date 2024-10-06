from django.shortcuts import render

def SignUp(request):
    return render(request, 'signup/signup.html')