from django import forms

class Register(forms.Form):
    name = forms.CharField(max_length=30)
    user_name = forms.CharField(max_length=15)
    gender = forms.IntegerField()
    profile = forms.ImageField()
    email = forms.EmailField()
    password = forms.PasswordInput()