from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer


class PostView(viewsets.ModelViewSet):
    """CRUD for Post entity"""

    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Set current user as author of post"""

        serializer.save(author=self.request.user)


class LikeView(viewsets.ModelViewSet):
    """CRUD for Like entity"""

    permission_classes = (IsAuthenticated,)
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        """Set current user as author of post"""

        serializer.save(author=self.request.user)
