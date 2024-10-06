from rest_framework import serializers
from .models import SignUp
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from django.utils.translation import gettext_lazy as _

class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=SignUp.objects.all())]    
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=SignUp.objects.all())]
    )
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = SignUp
        fields = ['username','email','password1','password2','first_name','last_name']

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({'password':'The passwords provided are different!'})
        return attrs
    
    def create(self,validated_data):
        user = SignUp.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password1'])
        user.save()

        return user