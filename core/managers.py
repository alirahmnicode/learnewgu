from django.db import models


class VocabManager(models.Manager):
    def get_queryset(self, owner=None):
        queryset = super().get_queryset().order_by('-created')
        if owner is not None:
            return queryset.filter(user=owner)
        else:
            return queryset.order_by('-created')

    def all(self, owner=None):
        if owner == None:
            return self.get_queryset()
        else:
            return self.get_queryset(owner=owner)

    def get_words(self, owner=None):
        return self.get_queryset(owner=owner).filter(type='word')

    def get_phrases(self, owner=None):
        return self.get_queryset(owner=owner).filter(type='phrase')

    def get_recent_obj(self, owner=None):
        return self.get_queryset(owner=owner)