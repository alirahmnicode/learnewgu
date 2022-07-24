from django.urls import path
from .views import CreateCategoryView, DetailCategoryView, CategoryUpdateView, CategoryDeleteView


app_name = 'category'

urlpatterns = [
    path('add/', CreateCategoryView.as_view(), name="add"),
    path('detail/<int:pk>/', DetailCategoryView.as_view(), name="detail"),
    path('edit/<int:pk>/', CategoryUpdateView.as_view(), name="edit"),
    path('delete/<int:pk>/', CategoryDeleteView.as_view(), name="delete"),
]