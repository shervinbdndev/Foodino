from django import forms
from django.core import validators
    
    

    
    

class RegisterForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=64,
        required=True,  
        label='نام کاربری',
        validators=[
            validators.MinLengthValidator(limit_value=3),
            validators.MaxLengthValidator(limit_value=64),    
        ],
        widget=forms.TextInput(attrs={
            'id': 'username',
            'placeholder': 'نام کاربری',
        },),
    )
    
    first_name = forms.CharField(
        min_length=3,
        max_length=64,
        required=True,  
        label='نام',
        validators=[
            validators.MinLengthValidator(limit_value=3),
            validators.MaxLengthValidator(limit_value=64),    
        ],
        widget=forms.TextInput(attrs={
            'id': 'fname',
            'placeholder': 'نام',
        },),
        
    )
    
    last_name = forms.CharField(
        min_length=3,
        max_length=64,
        required=True,  
        label='نام خانوادگی',
        validators=[
            validators.MinLengthValidator(limit_value=3),
            validators.MaxLengthValidator(limit_value=64),    
        ],
        widget=forms.TextInput(attrs={
            'id': 'lname',
            'placeholder': 'نام خانوادگی',
        },),
    )
    
    email = forms.EmailField(
        max_length=150,
        required=True,
        label='ایمیل',
        validators=[
            validators.EmailValidator(),
        ],
        widget=forms.EmailInput(attrs={
            'id': 'email',
            'placeholder': 'ایمیل',
        },),
    )
    
    password = forms.CharField(
        min_length=6,
        max_length=64,
        required=True,
        label='رمز ورود',
        validators=[
            validators.MinLengthValidator(limit_value=6),
            validators.MaxLengthValidator(limit_value=64),
        ],
        widget=forms.PasswordInput(attrs={
            'id': 'pass',
            'placeholder': 'رمز ورود',
        },),
    )
    
    con_password = forms.CharField(
        min_length=6,
        max_length=64,
        required=True,
        label='تایید رمز ورود',
        validators=[
            validators.MinLengthValidator(limit_value=6),
            validators.MaxLengthValidator(limit_value=64),
        ],
        widget=forms.PasswordInput(attrs={
            'id': 'conpass',
            'placeholder': 'تکرار رمز ورود ',
        },),
    )
    
    



class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=64,
        required=True,
        label='نام کاربری',
        validators=[
            validators.MinLengthValidator(limit_value=3),
            validators.MaxLengthValidator(limit_value=64),    
        ],
        widget=forms.TextInput(attrs={
            'id': 'username',
            'placeholder': 'نام کاربری',
        },),
    )
    
    password = forms.CharField(
        min_length=6,
        max_length=64,
        required=True,
        label='رمز ورود',
        validators=[
            validators.MinLengthValidator(limit_value=6),
            validators.MaxLengthValidator(limit_value=64),
        ],
        widget=forms.PasswordInput(attrs={
            'id': 'pass',
            'placeholder': 'رمز ورود',
        },),
    )