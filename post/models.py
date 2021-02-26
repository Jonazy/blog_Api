from django.db import models
from authentication.models import User
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, related_name='post_by', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=300, blank=False)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comment_by', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_comment', on_delete=models.CASCADE)
    detail = models.TextField(max_length=200, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.detail


class Like(models.Model):
    user = models.ForeignKey(User, related_name='like_by', on_delete=models.CASCADE)
    comment = models.ForeignKey(Post, related_name='comment_like', on_delete=models.CASCADE)
    like = models.BooleanField(max_length=1, default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
