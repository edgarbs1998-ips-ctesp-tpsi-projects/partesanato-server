# posts/serializers/post.py

from rest_framework.serializers import HyperlinkedModelSerializer

from posts.models import Post
from posts.serializers import PostCommentSerializer, PostImageSerializer, UserSerializer


class AdminPostSerializer(HyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'user_pk': 'user__pk',
    }

    user = UserSerializer(read_only=True)
    comments = PostCommentSerializer(many=True, read_only=True)
    images = PostImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            'url',
            'id',
            'user',
            'title',
            'description',
            'short_description',
            'approved',
            'likes',
            'dislikes',
            'datetime_created',
            'datetime_modified',
            'comments',
            'images',
        )
        read_only_fields = (
            'likes',
            'dislikes',
        )
        depth = 1


class PostSerializer(AdminPostSerializer):
    class Meta(AdminPostSerializer.Meta):
        read_only_fields = AdminPostSerializer.Meta.read_only_fields + (
            'approved',
        )
