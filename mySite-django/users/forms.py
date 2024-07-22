import this
from datetime import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': '    Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'id': 'form-pass', 'placeholder': '    Ваш пароль'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-regist', 'id': 'form_log', 'placeholder': '    Логин'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-regist', 'id': 'password_1', 'placeholder': '    Пароль'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-regist', 'id': 'password_2', 'placeholder': '    Повторите пароль'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email':'',
            'first_name': "",
            'last_name': "",
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-regist', 'id': 'form_email', 'placeholder': '    Email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-name', 'id': 'form_first', 'placeholder': '    Имя'}),
            'last_name': forms.TextInput(attrs={'class': 'form-name', 'id': 'form_last', 'placeholder': '    Фамилия'}),
        }

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError("Пароли не совпадают!")
    #     return cd['password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='', widget=forms.TextInput(attrs={'class': 'form-profile', 'id': 'profile_name'}))
    email = forms.CharField(disabled=True, label='', widget=forms.TextInput(attrs={'class': 'form-profile', 'id': 'profile_email'}))
    this_year = datetime.now().year
    date_birth = forms.DateField(label='', widget=forms.SelectDateWidget(years=tuple(range(this_year-100, this_year))))


    class Meta:
        model = get_user_model()
        fields = ['photo', 'username', 'email', 'date_birth', 'first_name', 'last_name']
        labels = {
            'photo': '',
            'first_name': "",
            'last_name': "",
        }
        widgets = {
            # 'photo': forms.FileInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-profile', 'id': 'profile_first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-profile', 'id': 'profile_last_name'}),
        }


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'password_profile_res', 'id': 'password_profile_res_old', 'placeholder': '    Старый пароль'}))
    # new_password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput(attrs={'class': 'password_profile_res', 'placeholder': '    Новый пароль'}))
    new_password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'password_profile_res', 'id': 'password_profile_res_1', 'placeholder': '    Новый пароль'}))
    new_password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'password_profile_res', 'id': 'password_profile_res_2', 'placeholder': '    Повторите новый пароль'}))






