from rest_framework import serializers
from apiregister.models import StudentClass,ClassDivision,Teacher,Student,StudentAttendance
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True,required=True,style={'input_type': 'password', 'placeholder': 'Password'})
    password2 = serializers.CharField(write_only=True,required=True,style={'input_type': 'password', 'placeholder': 'Password'})

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     r = User.objects.filter(username=username)
    #     if r.count():
    #         raise ValidationError("Username already exists")
    #     return username

    # def clean_password2(self):
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')

    #     if password1 and password2 and password1 != password2:
    #         raise ValidationError("Password don't match")

    #     return password2

    class Meta:
        model = User
        fields = [ 'first_name', 'username', 'password1', 'password2']