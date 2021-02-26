from rest_framework import serializers
from .models import User
from post.models import Post, Comment, Like


class UserSerializer(serializers.HyperlinkedModelSerializer):
    post_by = serializers.HyperlinkedRelatedField(many=True, view_name='post_detail', read_only=True)
    comment_by = serializers.HyperlinkedRelatedField(many=True, view_name='comment_detail', read_only=True)
    like_by = serializers.HyperlinkedRelatedField(many=True, view_name='like_detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'first_name', 'last_name', 'email', 'password', 'active',
                  'author', 'staff', 'admin', 'post_by', 'comment_by', 'like_by', ]
