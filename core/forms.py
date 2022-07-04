from django import forms
from .models import Vocabulary


class VocabulayForm(forms.ModelForm):
    class Meta:
        model = Vocabulary
        fields = ('text', 'translation', 'type')
        