from rest_framework import serializers

from .models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    """Serializer for Post model"""

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'created_at', 'author', 'likes')
        read_only_fields = ('id', 'likes')


class LikeSerializer(serializers.ModelSerializer):
    """Serializer for Like model"""

    class Meta:
        model = Like
        fields = ('post', 'created_at', 'author', 'value')


