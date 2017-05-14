from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm

from django.utils.translation import ugettext_lazy as _
from accounts.models import Account


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label=_("Email"),
        strip=False,
        required=True,
    )

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        strip=False,
        widget=forms.PasswordInput(),
    )

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            return

        if Account.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Account with this email already exists.')

        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "Passwords don't match",
                code='password_mismatch'
            )

        password_validation.validate_password(password2)

        return password2

    def save(self, commit=True):
        user = Account(
            email=self.cleaned_data.get('email'),
        )
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()

        return user


class LoginForm(AuthenticationForm):
    email = forms.EmailField(
        label=_("Email"),
        strip=False,
        required=True,
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(),
    )

    error_messages = {
        'invalid_login': _(
            "Please enter a correct username and password. Note that password "
            "field is case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }

    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
