from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


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
