from django.db import models

from ._base import BaseModel, BaseManager


class BitpinPostManager(BaseManager):
    def get_queryset(self):
        return super(BitpinPostManager, self).get_queryset().prefetch_related("rates")


class Post(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=False, blank=False, unique=True)
    content = models.TextField(null=False, blank=False)
    auther = models.CharField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return f"{self.title} By {self.auther}"

    class Meta:
        unique_together = ('title', 'auther')
