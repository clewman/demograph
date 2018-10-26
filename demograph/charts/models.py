from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.utils import timezone


class MapType(models.Model):
    maptype = models.CharField(max_length=100)

    def __str__(self):
        return self.maptype


