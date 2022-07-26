from rest_framework.serializers import Serializer, ModelSerializer
from core.models import Vocabulary


class VocabSerializer(ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = ('text', 'type')