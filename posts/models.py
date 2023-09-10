from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    likes = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='webs',
        on_delete=models.CASCADE
    )


class Comment(models.Model):
    content = models.TextField()
    web = models.ForeignKey(
        'Post',
        related_name='comments',
        on_delete=models.CASCADE
    )
    commenter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='posts',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.commenter
