from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=120)
    url = models.CharField(max_length=5000)
    text = models.CharField(max_length=10000)
    def __str__(self):
        return self.title



