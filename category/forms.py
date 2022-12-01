from django import forms
from .models import Category
from core.models import Vocabulary


class CategoryForm(forms.ModelForm):

    def __init__(self, q, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""
        super(CategoryForm, self).__init__(*args, **kwargs)
        if q:
            self.fields['vocabs'].queryset = q

    class Meta:
        model = Category
        fields = ('name', 'vocabs')