from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import UpdateView, DeleteView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from .models import Vocabulary
from .forms import VocabulayForm
from .filters import VocabFilter
from .listing_obj import Listing


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


class ListVocabView(View):

    def get(self, request, **kwargs):

        end_articles = request.GET.get('n')
        # if request not ajax
        if not end_articles:
            f = VocabFilter(self.request.GET, queryset=Vocabulary.objects.all())
            return render(request, 'core/list.html', {'filter':f})
        # if send request with ajax
        else:
            objs = Vocabulary.objects.all()
            listing = Listing(objs=objs)
            listing.range_of_objects(10, end_articles)
            data = listing.get_objects()
            return JsonResponse({'objects': data})


class ReviewVocab(View):
    def post(self, request, **kwargs):
        vocab = get_object_or_404(Vocabulary, pk=kwargs['pk'])
        count = vocab.review()
        return JsonResponse({'count':count})
    