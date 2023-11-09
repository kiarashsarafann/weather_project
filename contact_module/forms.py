from django import forms
from .models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your name...'
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Email Address...'
            }),
            'company': forms.TextInput(attrs={
                'placeholder': 'Company name...'
            }),
            'website': forms.TextInput(attrs={
                'placeholder': 'Website...'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Message'
            })
        }
