# posts/views/user.py

from django.contrib import auth
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from posts.permissions import IsAdminOrReadOnly
from posts.serializers import AdminUserSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = auth.get_user_model().objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = (
        IsAdminOrReadOnly,
    )
