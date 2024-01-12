# forms.py
from django import forms
from .models import ContactForm

class ContactFormModel(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['email', 'textarea', 'file']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Your email validation logic here
        return email
