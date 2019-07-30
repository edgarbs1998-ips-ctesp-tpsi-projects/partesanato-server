# posts/migrations/post.py

from django.contrib import auth
from django.db import models
from django.template.defaultfilters import truncatechars


class Post(models.Model):
    user = models.ForeignKey(
        verbose_name='posted by',
        to=auth.get_user_model(),
        on_delete=models.CASCADE,
        related_name='posts',
        related_query_name='posts',
    )
    title = models.CharField(
        max_length=80,
        unique=True,
    )
    description = models.TextField(
        max_length=6000,
    )
    approved = models.BooleanField(
        default=False,
        help_text='Designates whether this post will be visible to regular users.',
    )
    likes = models.PositiveIntegerField(
        default=0,
    )
    dislikes = models.PositiveIntegerField(
        default=0,
    )
    datetime_created = models.DateTimeField(
        verbose_name='created at',
        auto_now_add=True,
    )
    datetime_modified = models.DateTimeField(
        verbose_name='modified at',
        auto_now=True,
    )

    def short_description(self):
        return truncatechars(self.description, 120)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = (
            '-datetime_created',
        )
