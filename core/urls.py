from django.urls import path
from .views import Dashboard, AddObject


app_name = 'core'

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('add/', AddObject.as_view(), name="add-object")
]