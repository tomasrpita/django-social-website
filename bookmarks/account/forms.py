from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ["username", "first_name", "email"]

    # You can provide a clean_<fieldname>() method to any of your form fields
    # to clean the value or raise form validation errors
    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match.")
        return cd["password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Email already in use.")
        return email


class UserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email"]


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["date_of_birth", "photo"]

    def clean_email(self):
        email = self.cleaned_email["email"]
        qs = User.objects.exclude(id=self.instance.id).filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email already in use.")
        return email
