from django import forms
from django.contrib.auth import forms as auth_forms

from users.models import User

class SignUpForm(auth_forms.UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]
