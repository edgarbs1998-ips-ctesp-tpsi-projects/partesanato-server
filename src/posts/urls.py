# posts/urls.py

from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from posts.views import UserViewSet, PostViewSet, CommentViewSet, ImageViewSet, UserPostViewSet

router = SimpleRouter()
router.register('users', UserViewSet, base_name='user')
router.register('posts', PostViewSet, base_name='post')

users_router = NestedSimpleRouter(router, 'users', lookup='user')
users_router.register('posts', UserPostViewSet, base_name='user-post')

posts_router = NestedSimpleRouter(router, 'posts', lookup='post')
posts_router.register('comments', CommentViewSet, base_name='comment')
posts_router.register('images', ImageViewSet, base_name='image')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(users_router.urls)),
    path('', include(posts_router.urls)),
]
