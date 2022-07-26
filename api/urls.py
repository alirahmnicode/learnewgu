from django.urls import path
from .views import VocabularyListApiView


urlpatterns = [
    path('', VocabularyListApiView.as_view())
]