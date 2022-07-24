from django.urls import path
from .views import CreateCategoryView, DetailCategoryView


app_name = 'category'

urlpatterns = [
    path('add/', CreateCategoryView.as_view(), name="add"),
    path('detail/<int:pk>/', DetailCategoryView.as_view(), name="detail")
]