# posts/serializers/post_comment.py

from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

from posts.models import Comment
from posts.serializers import UserSerializer


class PostCommentSerializer(NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'post_pk': 'post__pk',
    }

    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'url',
            'id',
            'post',
            'user',
            'comment',
            'short_comment',
            'datetime_created',
            'datetime_modified',
        )
        read_only_fields = (
            'post',
        )
