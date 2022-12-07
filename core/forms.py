from django import forms
from django.forms import inlineformset_factory
from .models import Vocabulary, Sentence


class VocabulayForm(forms.ModelForm):
    class Meta:
        model = Vocabulary
        fields = ('word', 'translation')
        widgets = {
            'word': forms.TextInput(attrs={'maxlength':'200', 'autocomplete':'off', 'class':'text-trns'}),
            'translation': forms.Textarea(attrs={'cols':'30', 'rows':'1', 'class':'word-translation'})
        }
        
        
class SentenceForm(forms.ModelForm):
    class Meta:
        model = Sentence
        fields = ('text', 'translation')
        widgets = {
            'text': forms.Textarea(attrs={'cols':'30', 'rows':'1', 'class':'text-trns'}),
            'translation': forms.Textarea(attrs={'cols':'30', 'rows':'1'})
        }


SentenceInlineFormset = inlineformset_factory(
    parent_model=Vocabulary, model=Sentence, 
    form=SentenceForm, extra=1, can_delete=True)
