from django.urls import path
from authentication import views

urlpatterns = [
    path('', views.UserViewSet.as_view()),
    path('<int:pk>/', views.UserDetailSet.as_view()),
]
