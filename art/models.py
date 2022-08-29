from django.db import models
#from django.contrib.auth.models import user
from django.conf import settings


class Artist(models.Model):
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='artists')

    def __str__(self):
        return self.account.username


class Art(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    price = models.IntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='arts')

    def __str__(self):
        return self.title