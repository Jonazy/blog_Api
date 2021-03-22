from django.shortcuts import render
# from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment, PostLike
from .serializers import PostSerializer, CommentSerializer, LikePostSerializer
from rest_framework import generics, permissions
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.exceptions import PermissionDenied
from .permissions import IsAuthorOrReadOnly


# Create your views here.


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.filter(published=True)
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        queryset = Post.objects.filter(published=True)
        return queryset

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class CommentList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Comment.objects.filter(post=self.kwargs['pk'])
        return queryset

    # queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        queryset = Comment.objects.filter(id=self.kwargs['pk'])
        return queryset

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


# class LikeList(APIView):
#     serializer_class = LikeSerializer
#
#     def get_queryset(self):
#         queryset = Like.objects.filter(post_id=self.kwargs['pk'])
#         return queryset
#
#     def post(self, request, pk, cmt_pk):
#         user = self.request.user
#         likes = Like.objects.all()
#         # data = {'user': user.pk, 'like': likes}
#         serializer = LikeSerializer(data=request.data)
#         if serializer.is_valid():
#             if likes.filter(like=True):
#                 serializer.save(like=False)
#             else:
#                 serializer.save(like=True)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def perform_create(self, serializer):
#
#         serializer.save(user=self.request.user)

#
# class LikePost(generics.CreateAPIView, generics.DestroyAPIView):
#     serializer_class = LikePostSerializer
#     queryset = PostLike.objects.all()
#     # def get_queryset(self):
#     #     queryset = PostLike.objects.filter(user=self.request.user)
#     #     return queryset
#
#     # def post(self, request, pk):
#     #     # user = self.request.user
#     #     like = PostLike.objects.filter(user=self.request.user)
#     #     # data = {'user': user.pk, 'like': likes}
#     #     # single_user = like.filter(user=self.request.user)
#     #     if like.exists():
#     #         like.remove()
#     #     else:
#     #         serializer = LikePostSerializer(data=request.data)
#     #         if serializer.is_valid():
#     #             serializer.save()
#     #             return Response(serializer.data, status=status.HTTP_201_CREATED)
#     #         else:
#     #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def like(self, request):
#         queryset = PostLike.objects.filter(user=self.request.user)
#         if queryset.exists():
#
#             def perform_delete(serializer):
#                 serializer.delete(user=self.request.user)
#
#     def perform_create(self, serializer):
#         queryset = PostLike.objects.filter(user=self.request.user)
#         # like_id = PostLike.objects.filter(id=id)
#         if queryset.exists():
#             serializer.save()
#         else:
#             serializer.save(user=self.request.user)
#

