from django.shortcuts import render
from .serializers import LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token


def Login(request):
    return render(request, 'login/login.html')

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({"message":"Login successful", "user_id":user.id})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






