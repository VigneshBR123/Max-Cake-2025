from django import forms

from .models import Profile

class LoginForm(forms.Form):

    username = forms.CharField(max_length=50, widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': "Enter your email",
        'required': 'required'
    }))

    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': "Enter your password",
        'required': 'required'
    }))

class RegisterForm(forms.ModelForm):

    class Meta:

        model = Profile

        fields = ['email', 'first_name', 'last_name', 'phone_num']

        widgets = {

            'email': forms.EmailInput(attrs={'class':'form-control','required':'required'}),

            'first_name': forms.TextInput(attrs={'class':'form-control','required':'required'}),

            'last_name': forms.TextInput(attrs={'class':'form-control','required':'required'}),

            'phone_num': forms.TextInput(attrs={'class':'form-control','required':'required'})

        }