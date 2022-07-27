import random
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from core.models import Vocabulary
from core.ajax import is_ajax


class FillingView(View):
    def get(self, request, **kwargs):
        words = Vocabulary.objects.filter(type='word')
        word = random.choice(words)
        if is_ajax(request):
            word = word.values('pk', 'text', 'translation',
                        'type', 'review_count', 'created')
            return JsonResponse(data=word)
        else:
            if kwargs['pk']:
                word = get_object_or_404(Vocabulary, kwargs['pk'])
            context = {
                'word':word
            }
            return render(request, 'dictation/fill.html', context)