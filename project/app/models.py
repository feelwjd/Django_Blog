from django.db import models
from django.db.models.base import Model

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    writer = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.title