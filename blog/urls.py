from django.urls import path
from .views import FeedView, like_view, CreatePostView

app_name = 'blog'

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    path('post/<int:post_id>/', FeedView.as_view(), name='feed_page_with_pk'),
    path('like/<int:post_id>/', like_view, name='like_post'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
]
