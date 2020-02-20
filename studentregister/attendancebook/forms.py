from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from attendancebook.models import StudentClass,ClassDivision,Teacher,Student,StudentAttendance
from django.contrib.auth.forms import AuthenticationForm


class UserForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    class Meta:
        model = User
        fields = ['first_name','username','password1', 'password2']


class ClassDivisionForm(forms.ModelForm):

    class Meta:
        model = ClassDivision
        fields = ['division_name']


class StudentClassForm(forms.ModelForm):

    class Meta:
        model = StudentClass
        fields = ['student_classname']
        

class LoginForm(AuthenticationForm):

    class Meta:
        fields= ['username','password']

