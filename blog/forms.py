from django import forms


class SearchForm(forms.Form):
    """Form for blog search functionality"""
    q = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control me-2',
            'placeholder': 'Search posts...',
            'aria-label': 'Search'
        })
    )
