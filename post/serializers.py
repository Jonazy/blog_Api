from rest_framework import serializers
from .models import Post, Comment, Like


class PostSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source='author.first_name')
    # comment_by = serializers.HyperlinkedRelatedField(many=True, view_name='comment_detail', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'slug', 'description', 'published', 'created', 'updated']


class CommentSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.first_name')

    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'detail', 'created', 'updated']


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ['id', 'user', 'comment', 'like', 'created', 'updated']