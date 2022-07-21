from django.db import models
from django.contrib.auth.models import User
from .managers import VocabManager


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

    def review(self):
        self.review_count += 1
        self.save()
        return self.review_count
        
    def __str__(self):
        return self.text[:20]


class Category(models.Model):
    name = models.CharField(max_length=300)
    vocabs = models.ManyToManyField(Vocabulary, related_name='v', verbose_name='Vocabulary')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name