from django.views.generic import View, DetailView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Category
from .forms import CategoryForm
from core.models import Vocabulary


class CategoryListView(ListView):
    template_name = 'category/list.html'
    
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CreateCategoryView(View):
    def post(self, request):
        form = CategoryForm(None, request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = self.request.user
            obj.save()
            # save vocabs
            for v in form.clean()['vocabs'].all():
                obj.vocabs.add(v)
            return redirect('category:list')

    def get(self, request, *args, **kwargs):
        vocabs = Vocabulary.objects.all(owner=request.user)
        form = CategoryForm(q=vocabs)
        context = {
            "vocabs":vocabs,
            "form":form
        }
        return render(request, 'category/add.html', context)


class DetailCategoryView(DetailView):
    template_name = 'category/detail.html'

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user, pk=self.kwargs['pk'])


class CategoryUpdateView(UpdateView):

    template_name = 'category/edit.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category:list')

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
            This is necessary to only display members that belong to a given user"""
        kwargs = super(CategoryUpdateView, self).get_form_kwargs()            
        kwargs['request'] = self.request
        return kwargs


class CategoryDeleteView(DeleteView):
    template_name = 'category/delete.html'
    model = Category
    success_url = reverse_lazy('category:list')