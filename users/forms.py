from django import forms
from users.models import User

class Register(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Name', 'University', 'Address', 'Email']
        widgets = {
            'Password': forms.PasswordInput(),
        }

class Login(forms.ModelForm):
    model = User
    fields = ['Email']
    widgets = {
        'Password': forms.PasswordInput()
    }