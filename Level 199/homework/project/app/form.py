from django import forms

class RegisterForm(forms.form):
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    email = forms.EmailInput(widget=forms.EmailInput())
    age = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput())
    phone =  forms.CharField()