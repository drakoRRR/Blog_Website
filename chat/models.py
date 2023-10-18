from django.db import models

from users.models import User


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms2')


class Message(models.Model):
    room = models.ForeignKey(to=Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
