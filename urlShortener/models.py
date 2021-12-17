from django.db import models

# Create your models here.

class Url(models.Model):
    url = models.URLField(max_length=250, unique = True)
    shortUrl = models.CharField(max_length = 30, unique = True)
    premiumType = models.BooleanField()
    exp_date = models.DateTimeField()
    visited = models.IntegerField(null = True)

    def __str__(self):
        return self.url
