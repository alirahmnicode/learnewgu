import random
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
from .ajax import is_ajax


class Dashboard(View):
    def get(self, request):
        obj_list = Vocabulary.objects.get_recent_obj()
        return render(request, 'core/dashboard.html', {'obj_list':obj_list})


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
    success_url = '/'


class DetailVocabView(DetailView):

    template_name = 'core/detail.html'

    def get_queryset(self):
        return Vocabulary.objects.filter(user=self.request.user)


class ListVocabView(View):

    def get(self, request, **kwargs):

        end_articles = request.GET.get('n')
        # if request not ajax
        if not end_articles:
            f = VocabFilter(self.request.GET, 
                queryset=Vocabulary.objects.get_recent_obj(owner=request.user))
            return render(request, 'core/list.html', {'filter':f})
        # if send request with ajax
        else:
            queryset = Vocabulary.objects.all(owner=request.user)
            listing = Listing(queryset=queryset)
            listing.range_of_objects(15, end_articles)
            data = listing.get_objects()
            return JsonResponse({'objects': data})


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
