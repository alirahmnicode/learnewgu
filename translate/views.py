from django.http import JsonResponse
from .translate import GoogleTranslate


def translate(request):
    primary_text = request.GET.get('text')
    gt = GoogleTranslate(text=primary_text, target='fa', source='en')
    translated = gt.translate()
    data = {
        'tr_text': translated
    }
    return JsonResponse(data)