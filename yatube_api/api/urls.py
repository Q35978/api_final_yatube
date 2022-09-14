# yatube_api/api/urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    PostViewSet,
    GroupViewSet,
    CommentViewSet,
    FollowViewSet,
)

router_for_v1 = DefaultRouter()
router_for_v1.register(
    'posts',
    PostViewSet,
    basename='posts'
)
router_for_v1.register(
    'groups',
    GroupViewSet,
    basename='groups'
)
router_for_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_for_v1.register(
    'follow',
    FollowViewSet,
    basename='followers'
)
urlpatterns = [
    path(
        'v1/',
        include(router_for_v1.urls),
    ),
    path('v1/',
         include('djoser.urls')
         ),
    path('v1/',
         include('djoser.urls.jwt')
         ),
]
