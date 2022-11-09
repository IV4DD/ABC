from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Account
from crispy_forms.helper import FormHelper
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.forms import ModelForm


# Capitalization of Input
class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()
class CapitalizeInputForm(forms.CharField):
    def to_python(self, value):
        return value.capitalize()



class AccountAuthenticateForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username', 'password')
        field_classes = {"username": UsernameField}

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Телефон',
                    'data-mask': '(000) 000 00 00',
                }
            ),
        }

    def clean(self):
        try:
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid phone or password.")
        except KeyError:
            raise forms.ValidationError('Invalid credentials')


class AccountCreationForm(UserCreationForm):
    """
    A form that creates an account, with no privileges
    """

    first_name = CapitalizeInputForm(
        label='Имя',
        max_length=20,
        min_length=2,
        validators=[RegexValidator(r'^[а-яА-Яё\s]*$', message="Допустимы только кириллические буквы!")],
        widget=forms.TextInput(attrs={
            'placeholder': 'Имя...',
            'style': 'font-size: 15px; text-transform: capitalize;'
        })
    )
    middle_name = CapitalizeInputForm(
        label='Отчество',
        max_length=20,
        min_length=2,
        validators=[RegexValidator(r'^[а-яА-Яё\s]*$', message="Допустимы только кириллические буквы!")],
        widget=forms.TextInput(attrs={
            'placeholder': 'Отчество...',
            'style': 'font-size: 15px; text-transform: capitalize;'
        })
    )
    surname = CapitalizeInputForm(
        label='Ваша фамилия',
        max_length=20,
        min_length=2,
        validators=[RegexValidator(r'^[а-яА-Яё\s]*$', message="Допустимы только кириллические буквы!")],
        widget=forms.TextInput(attrs={
            'placeholder': 'Фамилия...',
            'style': 'font-size: 15px; text-transform: capitalize;'
        })
    )

    email = Lowercase(
        label='E-mail',
        max_length=50,
        min_length=7,
        required=True,
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
                                   message="Проверьте правильность ввода E-Mail адресса!")],
        widget=forms.TextInput(attrs={
            'placeholder': 'E-mail',
            'style': 'font-size: 15px; text-transform: lowercase;'
        })
    )
    password1 = forms.CharField(
        label="Введите пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль',
            "autocomplete": "off"
        }),
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Повторите пароль',
            'autocomplete': 'off'
        }),
    )

    class Meta:
        model = Account
        fields = ("username", "first_name", "middle_name", "surname", "email", "dob", "status",)
        field_classes = {"username": UsernameField}

        STATUSES = (
            ('На рассмотрении', 'На рассмотрении'),
            ('Утвержден', 'Утвержден'),
            ('Отклонен', 'Отклонен'),
        )

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Телефон',
                    'data-mask': '(000) 000 00 00',
                }
            ),
            'dob': forms.TextInput(
                attrs={
                    'placeholder': 'Дата рождения',
                    'data-mask': '00.00.0000',
                }
            ),
            'status': forms.Select(
                choices=STATUSES,
                attrs={
                    'class': 'form-control',
                }
            ),
        }


    def __init__(self, *args, **kwargs):
        super(AccountCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "autofocus"
            ] = True

