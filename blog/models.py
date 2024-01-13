from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    text = models.TextField()
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    def __str__(self):
        return self.title
class Comment(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)