from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import UpdateView, DeleteView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Vocabulary
from .forms import VocabulayForm


class Dashboard(View):
    def get(self, request):
        words = Vocabulary.objects.get_words()
        phrases = Vocabulary.objects.get_phrases()
        content = {
            'words':words,
            'phrases':phrases
        }
        return render(request, 'core/dashboard.html', content)


class AddObject(View):
    def get(self, request, **kwrags):
        form = VocabulayForm
        return render(request, 'core/add_object.html', {'form':form})

    def post(self, request, **kwrags):
        form = VocabulayForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect(request.META.get('HTTP_REFERER'))


class UpdateVocab(UpdateView):
    template_name = 'core/update.html'
    model = Vocabulary
    form_class = VocabulayForm
    success_url = '/'


class DeleteVocabView(DeleteView):
    template_name = 'core/vocab_delete.html'
    model = Vocabulary
    success_url = 'core:dashboard'


class DetailVocabView(DetailView):

    template_name = 'core/detail.html'

    def get_queryset(self):
        return Vocabulary.objects.filter(user=self.request.user)


class ListVocabView(ListView):

    template_name = 'core/list.html'
    model = Vocabulary
