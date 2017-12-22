from django.db import models

# Create your models here.
class currency(models.Model):
    symbol = models.CharField(max_length = 5)
    name = models.CharField(max_length = 10)
    icon_absolute_link = models.CharField(max_length = 255)
    icon_relative_link = models.CharField(max_length = 255)
