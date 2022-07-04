from django.shortcuts import render, redirect
from django.views import View
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