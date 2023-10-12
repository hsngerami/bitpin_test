from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from ._base import BaseManager, BaseModel
from core.models import Post

User = get_user_model()


class RateManager(BaseManager):
    def get_queryset(self) -> models.query.QuerySet:
        return super().get_queryset().select_related("user", "post")


class Rate(BaseModel):
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rates")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="rates")
    objects = RateManager()

    def __str__(self):
        return f"{self.owner.username} gave score: {self.score} to post: {self.post.title} by {self.post.author}"

    class Meta:
        unique_together = ('owner', 'post')
