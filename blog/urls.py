from django.urls import path
from .views import FeedView, like_view

app_name = 'blog'

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    path('post/<int:post_id>/', FeedView.as_view(), name='feed_page_with_pk'),
    path('like/<int:post_id>/', like_view, name='like_post'),
]
