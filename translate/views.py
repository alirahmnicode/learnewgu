from django.http import JsonResponse
from django.shortcuts import render
from .translate import translate_text


def translate(request):
    text = request.GET.get('text')
    return JsonResponse(translate_text(text, 'fa'), safe=False)