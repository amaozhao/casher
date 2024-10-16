import uuid
from django.db import models
from django.contrib.auth.models import User
from flow.models import FlowData


class UserUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=40, default=uuid.uuid4)
    name = models.CharField(max_length=20)
    subfolder = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["uid", ], name="user_up_uid_idx"),
        ]


class UserTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flow = models.ForeignKey(FlowData, on_delete=models.CASCADE)
    fee = models.IntegerField(default=10)
    prompt_id = models.CharField(max_length=50)
    status = models.CharField(max_length=100, default='queue')
    result = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_task'
        ordering = ["-updated"]
