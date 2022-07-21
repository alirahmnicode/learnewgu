from django.db import models
from django.contrib.auth.models import User
from core.models import Vocabulary


class Category(models.Model):
    name = models.CharField(max_length=300)
    vocabs = models.ManyToManyField(Vocabulary, related_name='v', verbose_name='Vocabulary')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name