from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import UserSerializer
from .models import User

# Create your views here.


class UserViewSet(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDetailSet(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

