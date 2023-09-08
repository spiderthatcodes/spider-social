from django.db import models
from django.conf import settings


class Detail(models.Model):
    avatar = models.URLField()
    species = models.CharField(max_length=200, null=True)
    spider = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.spider.username
