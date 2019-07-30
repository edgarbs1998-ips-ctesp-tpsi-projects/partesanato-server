# posts/migrations/post_image.py

from django.db import models

from posts.models import Post


def post_directory_path(instance, filename):
    # MEDIA_ROOT/images/user_<id>/post_<id>/<filename>
    return f'images/user_{instance.post.user.id}/post_{instance.post.id}/{filename}'


class Image(models.Model):
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name='images',
        related_query_name='image',
    )
    image = models.ImageField(
        width_field='image_width',
        height_field='image_height',
        upload_to=post_directory_path,
    )
    image_width = models.IntegerField()
    image_height = models.IntegerField()

    def __str__(self):
        return f'{self.image.url}'
