from django.urls import path
from django.views.generic import TemplateView
from .views import (Dashboard, 
                    AddObject, UpdateVocab, 
                    DeleteVocabView, DetailVocabView, 
                    ListVocabView, ReviewVocab,
                    RandomReview)


app_name = 'core'

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name="home"),
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('add/', AddObject.as_view(), name="add"),
    path('edit/<int:pk>/', UpdateVocab.as_view(), name="edit"),
    path('vocab/<int:pk>/delete/', DeleteVocabView.as_view(), name="delete"),
    path('vocab/<int:pk>/detail/', DetailVocabView.as_view(), name="detail"),
    path('vocab/list/', ListVocabView.as_view(), name="list"),
    path('vocab/review/<int:pk>/', ReviewVocab.as_view(), name="review"),
    path('vocab/random-review/', RandomReview.as_view(), name="random"),
]