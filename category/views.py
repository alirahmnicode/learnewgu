from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .models import Category
from .forms import CategoryForm


class CategoryListView(ListView):
    template_name = 'category/list.html'
    
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


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


class DetailCategoryView(DetailView):
    template_name = 'category/detail.html'

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user, pk=self.kwargs['pk'])


class CategoryUpdateView(UpdateView):

    template_name = 'category/edit.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('core:dashboard')

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
            This is necessary to only display members that belong to a given user"""
        kwargs = super(CategoryUpdateView, self).get_form_kwargs()            
        kwargs['request'] = self.request
        return kwargs


class CategoryDeleteView(DeleteView):
    template_name = 'category/delete.html'
    model = Category
    success_url = reverse_lazy('core:dashboard')