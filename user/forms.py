from django import forms


class UserRegisterForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "your username"}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "your email"}),
    )
    password = forms.CharField(
        min_length=6,
        max_length=100,
        widget=forms.PasswordInput(attrs={"placeholder": "your password"}),
    )



class UserLoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "your username"}),
    )
    password = forms.CharField(
        min_length=6,
        max_length=100,
        widget=forms.PasswordInput(attrs={"placeholder": "your password"}),
    )