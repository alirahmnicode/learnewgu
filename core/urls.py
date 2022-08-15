from django.urls import path
from .views import (IndexView,
                    Dashboard, 
                    AddObject, UpdateVocab, 
                    DeleteVocabView, 
                    listing, 
                    ReviewVocab,
                    RandomReview)


app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('add/', AddObject.as_view(), name="add"),
    path('vocab/<int:pk>/edit/', UpdateVocab.as_view(), name="edit"),
    path('vocab/<int:pk>/delete/', DeleteVocabView.as_view(), name="delete"),
    path('vocab/list/', listing, name="list"),
    path('vocab/review/<int:pk>/', ReviewVocab.as_view(), name="review"),
    path('vocab/random-review/', RandomReview.as_view(), name="random"),
]