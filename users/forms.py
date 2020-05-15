"""User forms."""

# Django
from django import forms


class ProfileForm(forms.Form):
    """Profile form."""
    
    # Atributos de nuestro furmulario
    website = forms.URLField(max_length=200, required=True)
    bigoraphy = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()