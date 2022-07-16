from atexit import register
from django import template

register = template.Library()

def url(value):
    url = ''
    if 'page' in value.split('&')[-1]:
        for v in value.split('&')[:-1]:
            url+=f'{v}&'
        url = url[:-1]
    else:
        url = value
    if ('review_count' in url) or ('type' in url) or ('text' in url):
        return url+'&'
    else:
        return url+'?'

register.filter('url', url)