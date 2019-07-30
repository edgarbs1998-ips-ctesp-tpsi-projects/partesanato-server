# posts/admin/image.py

from django.contrib import admin

from posts.models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
        'post',
        'image_width',
        'image_height',
    )
    readonly_fields = (
        'image_width',
        'image_height',
    )
    raw_id_fields = (
        'post',
    )
    search_fields = (
        'post__title',
        'image',
        'image_width',
        'image_height',
    )


admin.site.register(Image, ImageAdmin)
