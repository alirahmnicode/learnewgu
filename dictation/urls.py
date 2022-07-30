from django.urls import path
from .views import FillingView


app_name = 'dictaion'

urlpatterns = [
    path('filling/', FillingView.as_view(), name="filling")
]