from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StudentRegistration(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    conform_password=forms.CharField(widget=forms.PasswordInput)
    agree=forms.BooleanField(label='I Agree')
    address = forms.CharField(widget=forms.TextInput)
    choose_file = forms.FileField()

    def clean(self):
        cleaned_data=super().clean()
        valpass=cleaned_data['password']
        valepass=cleaned_data['conform_password']
        if valpass!=valepass:
            raise forms.ValidationError('password not match')

from . models import UserM

class Student_Registration(forms.ModelForm):
    class Meta:
        model = UserM
        fields=['name', 'email', 'password']
        labels={'name': 'Enter Name','password':'Enter Password','email': 'Enter Email'}
        help_text={'name': 'Enter your full name'}
        error_messages={'name': {'required': 'name compalsary'}}
        widgets={'password':forms.PasswordInput}




class Signupform(UserCreationForm):
    class Meta:
        model = User
        fields=['username','first_name','last_name','email']














