from django.db import models
from django.contrib.auth.models import User
from .managers import VocabManager


class Vocabulary(models.Model):
    word = models.CharField(max_length=100)
    translation = models.TextField()
    review_count = models.PositiveIntegerField(blank=True, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = VocabManager()

    def review(self):
        self.review_count += 1
        self.save()
        return self.review_count
        
    def __str__(self):
        return self.user.username


class Sentence(models.Model):
    text = models.TextField()
    translation = models.TextField()
    vocabulary = models.ForeignKey(Vocabulary, on_delete=models.CASCADE, 
                                        related_name='sentences')

    def __str__(self):
        return f'{self.text[:20]}...'