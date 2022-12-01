import django_filters
from .models import Vocabulary


class VocabFilter(django_filters.FilterSet):
    text = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Vocabulary
        fields = ('review_count',)