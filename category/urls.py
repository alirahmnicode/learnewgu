from django.urls import path
from .views import CreateCategoryView


app_name = 'category'

urlpatterns = [
    path('add/', CreateCategoryView.as_view(), name="add")
]