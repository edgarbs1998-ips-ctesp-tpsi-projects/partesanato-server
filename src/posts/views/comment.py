# posts/views/post_comment.py

from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from posts.models import Post, Comment
from posts.permissions import IsOwnerOrAdminOrReadOnly
from posts.serializers import PostCommentSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = PostCommentSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsOwnerOrAdminOrReadOnly,
    )
    filter_backends = (
        OrderingFilter,
    )
    ordering_fields = (
        ('user__username', 'Username'),
        ('datetime_created', 'Created at'),
        ('datetime_modified', 'Modified at'),
    )

    def get_queryset(self):
        return Comment.objects.filter(post__pk=self.kwargs['post_pk'])

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.kwargs['post_pk'])
        serializer.save(post=post, user=self.request.user)
