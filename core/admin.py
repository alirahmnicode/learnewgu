from django.contrib import admin
from .models import Vocabulary, Category

@admin.register(Vocabulary)
class VocabAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'type', 'user', 'created', 'review_count')
    list_filter = ('type', 'review_count',)
    search_fields = ('user__username', 'text')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')