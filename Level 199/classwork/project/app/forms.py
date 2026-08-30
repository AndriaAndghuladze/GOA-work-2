from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': "input-name"}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'color': 'blue'}, ), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), required=True)
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Age'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True)
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}), max_length=15, required=True)



class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())


class ProductForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'product-name'}),)
    price = forms.DecimalField(widget=forms.NumberInput())
    quantity = forms.IntegerField(widget=forms.NumberInput() )
    description = forms.CharField(widget=forms.Textarea(), )
    category = forms.ChoiceField()


class StudentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput())
    surname = forms.CharField(widget=forms.TextInput())
    age = forms.IntegerField(widget=forms.NumberInput())
    email = forms.EmailField(widget=forms.EmailInput())
    grade = forms.ChoiceField()


