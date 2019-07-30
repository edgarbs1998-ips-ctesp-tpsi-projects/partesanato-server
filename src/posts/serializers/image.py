# posts/serializers/post_image.py

from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

from posts.models import Image


class PostImageSerializer(NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'post_pk': 'post__pk',
    }

    class Meta:
        model = Image
        fields = (
            'url',
            'id',
            'post',
            'image',
            'image_width',
            'image_height',
        )
        read_only_fields = (
            'post',
            'image_width',
            'image_height',
        )
