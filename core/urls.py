from django.urls import path
from .views import Dashboard, AddObject, UpdateVocab


app_name = 'core'

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('add/', AddObject.as_view(), name="add-object"),
    path('edit/<int:pk>/', UpdateVocab.as_view(), name="update-vocab"),
]