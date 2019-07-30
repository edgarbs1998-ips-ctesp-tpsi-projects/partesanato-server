# posts/admin/comment.py

from daterange_filter.filter import DateRangeFilter
from django.contrib import admin

from posts.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'short_comment',
        'post',
        'user',
        'datetime_created',
        'datetime_modified',
    )
    list_filter = (
        ('datetime_created', DateRangeFilter),
        ('datetime_modified', DateRangeFilter),
    )
    raw_id_fields = (
        'post',
        'user',
    )
    search_fields = (
        'post__title',
        'user__username',
        'comment',
    )


admin.site.register(Comment, CommentAdmin)
