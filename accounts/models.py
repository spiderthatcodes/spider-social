from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Detail(models.Model):
    avatar = models.URLField(blank=True)
    species = models.CharField(max_length=250)
    spider = models.OneToOneField(UserModel,
        on_delete=models.CASCADE, null=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
