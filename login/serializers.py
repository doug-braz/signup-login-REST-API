from rest_framework import serializers
from signup.models import Account
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'password',]
