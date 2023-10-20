from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from chat.models import Room, Message
from users.models import User


# Create your views here.
class RoomDetailView(DetailView):
    model = Room
    template_name = 'chat/chat_page.html'

    def get_context_data(self, **kwargs):
        context = super(RoomDetailView, self).get_context_data(**kwargs)
        slug = self.kwargs['room_name']
        user1_id, user2_id = slug.split('-')
        user1 = get_object_or_404(User, pk=user1_id)
        user2 = get_object_or_404(User, pk=user2_id)

        room = Room.objects.filter(user1=user1, user2=user2).first()

        context['messages'] = Message.objects.filter(room=room)[0:25]
        context['user2'] = user2

        return context

    def get_object(self, queryset=None):
        slug = self.kwargs['room_name']
        user1_id, user2_id = slug.split('-')

        user1 = get_object_or_404(User, pk=user1_id)
        user2 = get_object_or_404(User, pk=user2_id)
        room = Room.objects.filter(user1=user1, user2=user2).first()

        print()

        if room:
            return room
        else:
            room = Room.objects.create(user1=user1,
                                       user2=user2,
                                       name=f'{user1.username} and {user2.username}',
                                       slug=f'{user1.id}-{user2.id}')
            return room
