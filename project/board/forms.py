from django import forms
from .models import Ppost


class PpostForm(forms.ModelForm):

    class Meta:
        model = Ppost
        fields = [
            'title',
            'text',
            'category',
        ]
