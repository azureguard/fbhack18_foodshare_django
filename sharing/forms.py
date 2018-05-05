from django import forms
from sharing.models import User, Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('university', 'address')


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ()
        widget = {
            'password': forms.PasswordInput(),
        }

