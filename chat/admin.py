from django.contrib import admin

from chat.models import Room, Message


# Register your models here.
@admin.register(Room)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'user1', 'user2']
    fields = ['name', 'slug', 'user1', 'user2']


@admin.register(Message)
class PostAdmin(admin.ModelAdmin):
    list_display = ['room', 'user', 'content', 'date_added']
    fields = ['room', 'user', 'content', 'date_added']
    readonly_fields = ['date_added']

