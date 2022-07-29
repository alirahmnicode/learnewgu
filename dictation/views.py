from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from core.models import Vocabulary
from core.ajax import is_ajax


class FillingView(View):
    def get(self, request, **kwargs):
        pk = request.GET.get('pk')
        if is_ajax(request):
            word = Vocabulary.objects.get_random_item(owner=request.user, filter_by='word', values=True)
            return JsonResponse(data=word, safe=False)
        else:
            word = Vocabulary.objects.get_random_item(owner=request.user, filter_by='word', values=False)
            if pk:
                word = get_object_or_404(Vocabulary, pk=pk)
            return render(request, 'dictation/fill.html', {'word':word})