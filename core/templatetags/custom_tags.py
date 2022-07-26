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
    if '?' in url:
        return url+'&'
    else:
        return url+'?'


def get_params(url, value):
    if value in url:
        return True


register.filter('url', url)
register.filter('params', get_params)