from django import forms
from .models import Contact_Us


class Contact_Us_form(forms.ModelForm):
    class Meta:
        model = Contact_Us
        fields = ['name', 'email', 'subject', 'about']