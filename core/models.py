from django.db import models
from django.contrib.auth.models import User


class VocabManager(models.Manager):
    def get_queryset(self, owner=None):
        queryset = super().get_queryset().order_by('-created')
        if owner is not None:
            return queryset.filter(user=owner)
        else:
            return queryset.order_by('-created')

    def all(self, owner=None):
        return self.get_queryset(owner=owner)

    def get_words(self, owner=None):
        return self.get_queryset(owner=owner).filter(type='word')

    def get_phrases(self, owner=None):
        return self.get_queryset(owner=owner).filter(type='phrase')

    def get_recent_obj(self, owner=None):
        return self.get_queryset(owner=owner)[:15]


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