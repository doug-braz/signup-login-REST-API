from django.shortcuts import render
from django.contrib.auth import login, logout
from .serializers import LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token



def Login(request):
    if not request.user.is_authenticated:
        return render(request, 'login/login.html')
    return render(request, 'homepage/home.html')

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response({"message":"Login successful", "user_id":user.id, "redirect_url":"/"})
        return Response(
                {"message":"Incorrect login or password. Please try again!",
                "errors": serializer.errors,}, 
                status=status.HTTP_400_BAD_REQUEST)

def Logout(request):
    logout(request)
    return render(request, 'homepage/home.html')




