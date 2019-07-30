# posts/migrations/post_comment.py

from django.contrib import auth
from django.db import models
from django.template.defaultfilters import truncatechars

from posts.models import Post


class Comment(models.Model):
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name='comments',
        related_query_name='comment',
    )
    user = models.ForeignKey(
        verbose_name='commented by',
        to=auth.get_user_model(),
        on_delete=models.CASCADE,
        related_name='comments',
        related_query_name='comment',
    )
    comment = models.TextField(
        max_length=2000,
    )
    datetime_created = models.DateTimeField(
        verbose_name='created at',
        auto_now_add=True,
    )
    datetime_modified = models.DateTimeField(
        verbose_name='modified at',
        auto_now=True,
    )

    def short_comment(self):
        return truncatechars(self.comment, 60)

    def __str__(self):
        return f'{self.comment}'

    class Meta:
        ordering = (
            '-datetime_created',
        )
