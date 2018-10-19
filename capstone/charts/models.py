from django.db import models


class Chart_Type(models.Model):
    user_choice = models.CharField(max_length=100)


    def __str__(self):
        return self.user_choice