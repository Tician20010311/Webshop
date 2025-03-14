from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm , SetPasswordForm
from django import forms
from .models import Profile

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label="Keresés")

class UserInfoForm(forms.ModelForm):
    telefon = forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control border-0 border-bottom rounded-0','placeholder': 'Telefonszám'}),required=False)
    cim1 = forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control border-0 border-bottom rounded-0','placeholder': 'Cím 1'}),required=False)
    cim2 = forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control border-0 border-bottom rounded-0','placeholder': 'Cím 1'}),required=False)
    iranyitoszam = forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control border-0 border-bottom rounded-0','placeholder': 'Irányítószám'}),required=False)
    varos = forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control border-0 border-bottom rounded-0','placeholder': 'Város'}),required=False)
    megye = forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control border-0 border-bottom rounded-0','placeholder': 'Megye'}),required=False)

    class Meta:
        model = Profile
        fields = ('telefon', 'cim1', 'cim2', 'iranyitoszam', 'varos', 'megye')


class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ('new_password1', 'new_password2')
    
    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        # Username mező


        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control border-0 border-bottom rounded-0',
        })
        self.fields['new_password1'].label = 'Jelszó'
        self.fields['new_password1'].help_text = ''

        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control border-0 border-bottom rounded-0',
        })
        self.fields['new_password2'].label = 'Jelszó mégegyszer'
        self.fields['new_password2'].help_text = ''

class UpdateUserForm(UserChangeForm):
    password = None
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(attrs={
            'class': 'form-control border-0 border-bottom rounded-0',
        })
    )
    first_name = forms.CharField(
        label="Vezetéknév",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control border-0 border-bottom rounded-0',
        })
    )
    last_name = forms.CharField(
        label="Keresztnév",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control border-0 border-bottom rounded-0',
        })
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')  # Jelszót töröltük

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        # Username mező
        self.fields['username'].widget.attrs.update({
            'class': 'form-control border-0 border-bottom rounded-0',
        })
        self.fields['username'].label = 'Felhasználónév'
        self.fields['username'].help_text = ''



class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(attrs={
            'class': 'form-control border-0 border-bottom rounded-0',
        })
    )
    first_name = forms.CharField(
        label="Vezetéknév",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control border-0 border-bottom rounded-0',
        })
    )
    last_name = forms.CharField(
        label="Keresztnév",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control border-0 border-bottom rounded-0',
        })
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # Username mező
        self.fields['username'].widget.attrs.update({
            'class': 'form-control border-0 border-bottom rounded-0',
            
        })
        self.fields['username'].label = 'Felhasználónév'
        self.fields['username'].help_text = ''

        # Jelszó mezők
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control border-0 border-bottom rounded-0',
        })
        self.fields['password1'].label = 'Jelszó'
        self.fields['password1'].help_text = ''

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control border-0 border-bottom rounded-0',
        })
        self.fields['password2'].label = 'Jelszó mégegyszer'
        self.fields['password2'].help_text = ''
