from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from chat.models import Room, Message
from users.models import User


# Create your views here.
#  Нужно создать представление, которое будет реагировать на кнопку message и будет создавать новый Room,
#  или если он уже создан то заходить в него
class RoomDetailView(DetailView):
    model = Room
    template_name = 'chat/chat_page.html'

    def get_context_data(self, **kwargs):
        context = super(RoomDetailView, self).get_context_data(**kwargs)
        user1 = get_object_or_404(User, pk=self.kwargs.get('user1'))
        user2 = get_object_or_404(User, pk=self.kwargs.get('user2'))
        room = Room.objects.filter(user1=user1, user2=user2).first()

        context['messages'] = Message.objects.filter(room=room)[0:25]

        return context

    def get_object(self, queryset=None):
        user1 = get_object_or_404(User, pk=self.kwargs.get('user1'))
        user2 = get_object_or_404(User, pk=self.kwargs.get('user2'))
        room = Room.objects.filter(user1=user1, user2=user2).first()

        if room:
            return room
        else:
            room = Room.objects.create(user1=user1,
                                       user2=user2,
                                       name=f'{user1.username} and {user2.username}',
                                       slug=f'{user1.id}{user2.id}')
            return room