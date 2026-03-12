from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Имя"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Фамилия"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["nickname", "avatar", "bio", "country", "birth_date"]
        widgets = {
            "nickname": forms.TextInput(attrs={"placeholder": "Никнейм"}),
            "bio": forms.Textarea(attrs={"rows": 4, "placeholder": "Расскажи немного о себе"}),
            "country": forms.TextInput(attrs={"placeholder": "Страна"}),
            "birth_date": forms.DateInput(attrs={"type": "date"}),
        }

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "placeholder": "Введите логин",
        })

        self.fields["password"].widget.attrs.update({
            "placeholder": "Введите пароль",
        })


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "placeholder": "Введите логин",
        })

        self.fields["password1"].widget.attrs.update({
            "placeholder": "Введите пароль",
        })

        self.fields["password2"].widget.attrs.update({
            "placeholder": "Повторите пароль",
        })