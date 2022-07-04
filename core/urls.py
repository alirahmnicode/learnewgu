from django.urls import path
from .views import Dashboard


app_name = 'core'

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name="dashboard")
]