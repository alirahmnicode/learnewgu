from django.contrib import admin
from .models import Vocabulary, Sentence

@admin.register(Vocabulary)
class VocabAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'created', 'review_count')
    list_filter = ('review_count',)
    search_fields = ('user__username', 'word')

admin.site.register(Sentence)