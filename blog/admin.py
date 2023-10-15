from django.contrib import admin
from.models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'text_post', 'posted')
    fields = ('author', 'posted', 'image', 'text_post', 'likes')
    readonly_fields = ('posted',)


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'date_added')
    fields = ('author', 'post', 'text', 'date_added')
    readonly_fields = ('date_added',)
