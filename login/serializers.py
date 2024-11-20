from rest_framework import serializers
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError('This account is inactive!')
                data['user'] = user
            else:
                raise serializers.ValidationError('Incorrect username or password. Please try again.')
        else:
            raise serializers.ValidationError('No fields shall be left in blank.')
        
        return data
