from django import forms


class SearchForm(forms.Form):
    city = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'find-location',
            'placeholder': 'Find your location...'
        })
    )
