from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from surveys.models import Company


class UserRegister(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]


class CompanyRegisterForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address_one', 'address_two']


class UserUpdateForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False

    class Meta:
        model = User
        fields = ['username', 'email']

    widgets = {
        'email': forms.EmailField(),
        'username': forms.TextInput()
    }



class UserProfileUpdateForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False

    class Meta:
        model = Profile
        fields = ['image','user_company']

