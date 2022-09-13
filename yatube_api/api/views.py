# yatube_api/api/views.py
from rest_framework import (
    filters,
    pagination,
    permissions,
    viewsets,
    generics,
    mixins,
)
from posts.models import Group, Post
from .permissions import IsAuthorOrReadOnlyPermission
from .serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    FollowSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission, )
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)
    pagination_class = None

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)
    pagination_class = None

    def get_post_object(self):
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, pk=post_id)

    def perform_create(self, serializer):
        post = self.get_post_object()
        serializer.save(
            author=self.request.user,
            post=post
        )


class ListCreateViewSet(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        viewsets.GenericViewSet
):
    pass


class FollowViewSet(ListCreateViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=user__username', '=following__username',)

    def get_queryset(self):
        user = self.request.user
        return user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
