import random
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import UpdateView, DeleteView, TemplateView
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Vocabulary
from .forms import VocabulayForm
from .filters import VocabFilter
from .sorting import SortObject
from .ajax import is_ajax
from category.models import Category


@method_decorator(login_required, name="dispatch")
class IndexView(TemplateView):
    def get(self, request):
        return redirect('core:dashboard')


class Dashboard(View):
    def get(self, request):
        obj_list = Vocabulary.objects.get_recent_obj(owner=request.user)
        categories = Category.objects.filter(user=request.user)
        return render(request, 'core/dashboard.html', {'obj_list':obj_list, 'categories':categories})


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
