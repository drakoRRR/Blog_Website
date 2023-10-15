from django.db import models

from users.models import User


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='users_posts', null=True, blank=True)
    text_post = models.TextField()
    likes = models.ManyToManyField(User, related_name='blog_post')

    def __str__(self):
        return f'Post id {self.id}, User {self.author.username}'

    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post {self.post.id}, User {self.author.username}, User comment {self.text[:20]}'
