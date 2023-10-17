from django.db import models

from users.models import User


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms2')
