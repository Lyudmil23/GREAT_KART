from django import forms

from GREAT_KART.accounts.models import Account


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
