from rest_framework import serializers
from .models import Account
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password

class AccountSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Account.objects.all())]    
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Account.objects.all())]
    )

    #* Passwords need to be write_only for safety reasons!
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Account
        fields = ['username','email','password1','password2','first_name','last_name']

    def validate(self, attrs): 
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({'password':'The passwords provided are different!'})
        return attrs
    
    def create(self,validated_data):
        password = validated_data.pop('password1') # The unhashed passwords is stored but is removed from validated_data
        validated_data.pop('password2')

        validated_data[password] = make_password(password) # This step hashes the password

        return Account.objects.create(**validated_data)