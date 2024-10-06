from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegistrationSerializer

def SignUp(request):
    return render(request, 'signup/signup.html')

class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)


