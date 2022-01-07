'''
here we will see to add email, name etc and all those
fields
a new form that inherits from usercrationform
so new file is this

meta class
this gives us nested namespace and keep config in one place
and we say in user model

after this go in views and add the form we just created

'''

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    #can give required=true for compulsory
    class Meta:
        model= User
        fields = ['username','email','password1','password2']

#form to update user model

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']

#now put it on profile views