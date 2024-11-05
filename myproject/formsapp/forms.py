from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact              # Specifies the model to use
        fields = ['name', 'email', 'message']  # Fields to include in the form
