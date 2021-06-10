"""Contact forms."""

# Django
from django import forms


class ContactForm(forms.Form):
    """Contact form."""

    name = forms.CharField(label="Nombre", required=True)
    email = forms.CharField(label="Email", required=True)
    content = forms.CharField(label="Contenido", widget=forms.Textarea)
    