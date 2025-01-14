from django import forms
from .models import Link

class LinkForm(forms.ModelForm): # clase mas form
    class Meta:
        model = Link
        fields = ['url', 'description'] # las colunas de la tabla