from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class FlowData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    workflow = models.TextField()
    prompt = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
