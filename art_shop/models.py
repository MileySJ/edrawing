from tabnanny import verbose
from django.db import models

# Create your models here.
class ArtSupplies(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Art Supplies'
        verbose_name_plural = 'Art Supplies'