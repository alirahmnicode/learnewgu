from django.db import models
from django.contrib.auth.models import User


class VocabManager(models.Manager):
    def get_words(self):
        return self.get_queryset().filter(type='word')

    def get_phrases(self):
        return self.get_queryset().filter(type='phrase')

class Vocabulary(models.Model):
    TYEPS_CHOICES = (
        ('word', 'word'),
        ('phrase', 'phrase')
    )
    text = models.CharField(max_length=750)
    translation = models.TextField()
    review_count = models.PositiveIntegerField(blank=True, default=0)
    type = models.CharField(choices=TYEPS_CHOICES, max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = VocabManager()

    def __str__(self):
        return self.text[:20]