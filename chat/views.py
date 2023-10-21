from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from chat.models import Room, Message
from users.models import User


# Create your views here.
class RoomDetailView(DetailView):
    model = Room
    template_name = 'chat/chat_page.html'

    def get_room_and_users(self):
        slug = self.kwargs['room_name']
        user1_id, user2_id = slug.split('-')
        user1 = get_object_or_404(User, pk=user1_id)
        user2 = get_object_or_404(User, pk=user2_id)
        room = Room.objects.filter(user1=user1, user2=user2).first()

        if not room:
            room = Room.objects.create(user1=user1,
                                       user2=user2,
                                       name=f'{user1.username} and {user2.username}',
                                       slug=f'{user1.id}-{user2.id}')
        return room, user1, user2

    def get_context_data(self, **kwargs):
        context = super(RoomDetailView, self).get_context_data(**kwargs)
        room, user1, user2 = self.get_room_and_users()

        context['messages'] = Message.objects.filter(room=room)[0:25]
        if user1.id > user2.id:
            context['user1'] = user1
            context['user2'] = user2
        else:
            context['user1'] = user2
            context['user2'] = user1

        return context

    def get_object(self, queryset=None):
        room, _, _ = self.get_room_and_users()
        return room



