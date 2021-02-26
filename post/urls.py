from django.urls import path
from post import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('<int:pk>/comments/', views.CommentList.as_view()),
    path('<int:pk>/comment/<int:cmt_pk>/', views.CommentDetail.as_view()),
    path('<int:pk>/comment/<int:cmt_pk>/like/', views.LikeList.as_view()),
]