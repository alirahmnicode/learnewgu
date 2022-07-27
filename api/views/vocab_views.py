from rest_framework import generics
from core.models import Vocabulary
from api.serializers import VocabSerializer


class VocabularyListView(generics.ListAPIView):
    queryset = Vocabulary.objects.all()
    serializer_class = VocabSerializer
