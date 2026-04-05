from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

TIMEZONE_CHOICES = [
    ('UTC', 'UTC'),
    ('Europe/Moscow', 'Europe/Moscow'),
    ('Europe/London', 'Europe/London'),
    ('America/New_York', 'America/New_York'),
]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    timezone = forms.ChoiceField(choices=TIMEZONE_CHOICES, initial='UTC')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Сохраняем профиль с timezone и email
            user.profile.timezone = self.cleaned_data['timezone']
            user.profile.email_encrypted = self.cleaned_data['email']
            user.profile.save()
        return user