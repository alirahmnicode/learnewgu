from rest_framework.generics import ListAPIView
from core.models import Vocabulary
from api.serializers import VocabSerializer


class VocabularyListApiView(ListAPIView):
    queryset = Vocabulary.objects.all()
    serializer_class = VocabSerializer
