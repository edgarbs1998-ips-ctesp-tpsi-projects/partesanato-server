# posts/views/post_image.py

from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from posts.models import Post, Image
from posts.permissions import IsPostOwnerOrAdminOrReadOnly
from posts.serializers import PostImageSerializer


class ImageViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = PostImageSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsPostOwnerOrAdminOrReadOnly,
    )

    def get_queryset(self):
        return Image.objects.filter(post__pk=self.kwargs['post_pk'])

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.kwargs['post_pk'])
        serializer.save(post=post)
