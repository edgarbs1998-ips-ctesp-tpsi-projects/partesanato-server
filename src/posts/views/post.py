# posts/views/post.py

from rest_framework import mixins
from rest_framework.decorators import detail_route
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from posts.models import Post
from posts.permissions import IsOwnerOrAdminOrReadOnly
from posts.serializers import PostSerializer, AdminPostSerializer


class PostViewSet(ModelViewSet):
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsOwnerOrAdminOrReadOnly,
    )
    filter_backends = (
        SearchFilter,
        OrderingFilter,
    )
    search_fields = (
        'title',
        'description',
        'user__username',
    )
    ordering_fields = (
        ('title', 'Title'),
        ('user__username', 'Username'),
        ('likes', 'Likes'),
        ('dislikes', 'Dislikes'),
        ('datetime_created', 'Created at'),
        ('datetime_modified', 'Modified at'),
    )

    @detail_route(methods=['get', 'post'], permission_classes=[IsAuthenticated])
    def likes(self, request, pk=None):
        likes = get_object_or_404(Post, pk=pk).likes
        if request.method == 'POST':
            likes += 1
            Post.objects.filter(pk=pk).update(likes=likes)
        return Response({'likes': likes})

    @detail_route(methods=['get', 'post'], permission_classes=[IsAuthenticated])
    def dislikes(self, request, pk=None):
        dislikes = get_object_or_404(Post, pk=pk).dislikes
        if request.method == 'POST':
            dislikes += 1
            Post.objects.filter(pk=pk).update(dislikes=dislikes)
        return Response({'dislikes': dislikes})

    def get_queryset(self):
        post = Post.objects.all()
        approved = self.request.query_params.get('approved', None)

        user_pk = None
        if self.kwargs:
            user_pk = Post.objects.get(pk=self.kwargs['pk']).user.pk

        if self.request.user and (
                self.request.user.pk == user_pk or self.request.user.is_staff) and approved is not None:
            post = post.filter(approved=approved)
        elif not self.request.user or not (self.request.user.pk == user_pk or self.request.user.is_staff):
            post = post.filter(approved=True)

        return post

    def get_serializer_class(self):
        if self.request.user and self.request.user.is_staff:
            return AdminPostSerializer
        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserPostViewSet(mixins.ListModelMixin,
                      GenericViewSet):
    serializer_class = PostSerializer
    filter_backends = (
        SearchFilter,
        OrderingFilter,
    )
    search_fields = (
        'title',
        'description',
    )
    ordering_fields = (
        ('title', 'Title'),
        ('likes', 'Likes'),
        ('dislikes', 'Dislikes'),
        ('datetime_created', 'Created at'),
        ('datetime_modified', 'Modified at'),
    )

    def get_queryset(self):
        user_pk = int(self.kwargs['user_pk'])
        post = Post.objects.filter(user__pk=user_pk)

        approved = self.request.query_params.get('approved', None)

        if self.request.user and (
                self.request.user.pk == user_pk or self.request.user.is_staff) and approved is not None:
            post = post.filter(approved=approved)
        elif not self.request.user or not (self.request.user.pk == user_pk or self.request.user.is_staff):
            post = post.filter(approved=True)

        return post
