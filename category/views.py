from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Category
from .forms import CategoryForm

# Create your views here.
class CreateCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/add.html'
    success_url = reverse_lazy('category:add')

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
            This is necessary to only display members that belong to a given user"""
        kwargs = super(CreateCategoryView, self).get_form_kwargs()            
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        self.obj = obj.save()
        return super().form_valid(form)