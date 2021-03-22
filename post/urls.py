from django.urls import path
from post import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    # path('<int:pk>/likes/', views.LikePost.as_view()),
    # path('<int:pk>/like/id', views.PostDetail.as_view()),
    path('<int:pk>/comment/', views.CommentList.as_view()),
    path('<int:pk>/comment/<int:cmt_pk>/', views.CommentDetail.as_view()),
    # path('<int:pk>/comment/<int:cmt_pk>/like/', views.LikeList.as_view()),
    # path('<int:pk>/comment/<int:cmt_pk>/like/lk_pk/', views.LikeDetail.as_view()),
]