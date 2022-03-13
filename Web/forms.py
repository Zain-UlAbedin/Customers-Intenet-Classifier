from django import forms


class RegistrationForm(forms.Form):
    FirstName = forms.CharField(max_length=100)
