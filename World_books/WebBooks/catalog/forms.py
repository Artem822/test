from django import forms
from datetime import date

class AuthorsForm(forms.Form):
    first_name = forms.CharField(label="Author's name")
    last_name = forms.CharField(label="Author's last name")
    date_of_birth = forms.DateField(label="Date of birth", widget=forms.widgets.DateInput(attrs={'type':'date'}))
    date_of_death = forms.DateField(label="Date of death", initial=format(date.today()), widget=forms.widgets.DateInput(attrs={'type':'date'}))