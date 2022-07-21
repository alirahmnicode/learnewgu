from django.contrib import admin
from .models import Vocabulary

@admin.register(Vocabulary)
class VocabAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'type', 'user', 'created', 'review_count')
    list_filter = ('type', 'review_count',)
    search_fields = ('user__username', 'text')
