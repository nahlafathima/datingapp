from django.forms import ModelForm, Form, TextInput, PasswordInput, CharField,EmailInput
from .models import User

class LoginFrom(Form):
    username = CharField(
        max_length = 15,
        min_length = 4,
        label = 'Username',
        required = True,
        widget = TextInput({
                'class': 'form-control'
            })
    )

    password = CharField(
        max_length = 25,
        min_length = 4,
        label = 'Password',
        required = True,
        widget = PasswordInput({
                'class': 'form-control'
            })
    )

class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","username","email","password"]
        widgets = {
            "first_name": TextInput({
                'class': 'form-control'
            }),
            "last_name": TextInput({
                'class': 'form-control'
            }),
            "username": TextInput({
                'class': 'form-control'
            }),
            "email": EmailInput({
                'class': 'form-control'
            }),
            "password": PasswordInput({
                'class': 'form-control'
            }),
        }