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


class CustomViewSet(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        viewsets.GenericViewSet
):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnlyPermission,
    )
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnlyPermission,
    )

    def get_post_object(self):
        id_post = self.kwargs.get('post_id')
        return generics.get_object_or_404(Post, id=id_post)

    def perform_create(self, serializer):
        post = self.get_post_object()
        serializer.save(
            author=self.request.user,
            post=post
        )

    def get_queryset(self):
        id_post = self.kwargs.get('post_id')
        post = generics.get_object_or_404(Post, id=id_post)
        return post.comments.all()


class FollowViewSet(CustomViewSet):
    serializer_class = FollowSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=user__username', '=following__username',)

    def get_queryset(self):
        user = self.request.user
        return user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
