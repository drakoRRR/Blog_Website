from django.contrib.auth.decorators import login_required
from django.urls import path

from chat.views import RoomDetailView

app_name = 'chat'

urlpatterns = [
    path('<slug:slug>/', login_required(RoomDetailView.as_view()), name='chat')
]
