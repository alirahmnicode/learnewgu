from django.urls import path
from .views import translate


app_name = 'translate'

urlpatterns = [
    path('text/', translate, name="text")
]