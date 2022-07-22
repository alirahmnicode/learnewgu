from django import forms
from .models import Category
from core.models import Vocabulary


class CategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.request = kwargs.pop('request')
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['vocabs'].queryset = Vocabulary.objects.filter(
            user=self.request.user
        )

    class Meta:
        model = Category
        fields = ('name', 'vocabs')