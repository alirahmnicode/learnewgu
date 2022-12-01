import random
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Vocabulary
from .forms import VocabulayForm, SentenceInlineFormset
from .filters import VocabFilter
from .sorting import SortObject
from .ajax import is_ajax
from category.models import Category


@method_decorator(login_required, name="dispatch")
class IndexView(TemplateView):
    def get(self, request):
        return redirect('core:list')


class VocabCreate(CreateView):
    form_class = VocabulayForm
    template_name = 'core/add_vocab.html'

    def get_context_data(self, **kwargs):
        ctx = super(VocabCreate, self).get_context_data(**kwargs)
        ctx['sentence_formset'] = SentenceInlineFormset()
        return ctx

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        sentence_formset = SentenceInlineFormset(self.request.POST)
        if form.is_valid() and sentence_formset.is_valid():
            return self.form_valid(form, sentence_formset)
        else:
            return self.form_invalid(form, sentence_formset)

    def form_valid(self, form, sentence_formset):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        # saving sentence Instances
        sentences = sentence_formset.save(commit=False)
        for sentence in sentences:
            sentence.vocabulary = self.object
            sentence.save()
        return redirect(("core:add"))

    def form_invalid(self, form, sentence_formset):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  sentence_formset=sentence_formset
                                  ))


class UpdateVocab(UpdateView):
    template_name = 'core/update.html'
    model = Vocabulary
    form_class = VocabulayForm
    success_url = '/'


class DeleteVocabView(DeleteView):
    template_name = 'core/vocab_delete.html'
    model = Vocabulary
    success_url = '/'


def listing(request):
    queryset = Vocabulary.objects.all(owner=request.user)
    filter = VocabFilter(request.GET, queryset=queryset)
    sorted_obj = SortObject(request.GET, queryset=filter.qs)
    paginator = Paginator(sorted_obj.qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)            
    context = {'page_obj': page_obj, 'filter_form':filter.form}
    return render(request, 'core/list.html', context)


class ReviewVocab(View):
    def post(self, request, **kwargs):
        vocab = get_object_or_404(Vocabulary, pk=kwargs['pk'])
        count = vocab.review()
        return JsonResponse({'count':count})
    

class RandomReview(View):
    def get(self, request):
        items = Vocabulary.objects.all(owner=request.user).values('pk', 'text', 'translation',
                                            'type', 'review_count', 'created')
        random_item = random.choice(items)
        if is_ajax(request):
            return JsonResponse({'object': random_item})
        else:
            return render(request, 'core/random_review.html', {'obj':random_item})


def check_word(request):
    word = request.GET.get('word')
    if word != '':
        w = Vocabulary.objects.filter(text=word)
        if w.count() > 0:
            return JsonResponse(False, safe=False)
        else:
            return JsonResponse(True, safe=False)

