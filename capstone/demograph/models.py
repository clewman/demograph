from django.db import models



class MapType(models.Model):
    map_type = models.CharField(max_length=50)


    def __str__(self):
        return self.map_type