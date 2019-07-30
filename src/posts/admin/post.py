# posts/admin/post.py

from daterange_filter.filter import DateRangeFilter
from django.contrib import admin

from posts.models import Post, Comment, Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = (
        'image_width',
        'image_height',
    )


class CommentInline(admin.TabularInline):
    model = Comment
    raw_id_fields = (
        'user',
    )


class PostAdmin(admin.ModelAdmin):
    inlines = (
        ImageInline,
        CommentInline,
    )
    list_display = (
        'id',
        'title',
        'user',
        'likes',
        'dislikes',
        'approved',
        'datetime_created',
        'datetime_modified',
    )
    list_filter = (
        'approved',
        ('datetime_created', DateRangeFilter),
        ('datetime_modified', DateRangeFilter),
    )
    raw_id_fields = (
        'user',
    )
    search_fields = (
        'title',
        'user__username',
        'description',
    )


admin.site.register(Post, PostAdmin)
