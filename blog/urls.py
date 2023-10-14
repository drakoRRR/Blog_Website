from django.urls import path
from .views import FeedView

app_name = 'blog'

urlpatterns = [
    path('', FeedView.as_view(), name='feed')
]
