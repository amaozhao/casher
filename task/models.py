import os

from django.contrib.auth.models import User
from django.db import models

from flow.models import WorkFlowData


def upload_cs_image_to(instance, filename):
    upload_dir = f"cs/images/"
    return os.path.join(upload_dir, filename)


def upload_cs_image_result(instance, filename):
    """
    自定义上传路径，根据 techsid 动态设置目录，防止文件名冲突
    """
    # 根据 techsid 创建目录
    upload_dir = f"result/images/"
    return os.path.join(upload_dir, filename)


class UserUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default="")
    image = models.ImageField(upload_to=upload_cs_image_to)
    subfolder = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated"]


class UserTask(models.Model):
    jilu_id = models.CharField(max_length=100)
    flow = models.ForeignKey(WorkFlowData, on_delete=models.CASCADE)
    fee = models.IntegerField(default=10)
    prompt_id = models.CharField(max_length=50, default="")
    image = models.ForeignKey(UserUpload, on_delete=models.CASCADE, null=True)
    prompt_text = models.TextField(default="")
    status = models.CharField(max_length=100, default="queue")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_task"
        indexes = [
            models.Index(
                fields=[
                    "prompt_id",
                ],
                name="prompt_id_idx",
            ),
            models.Index(
                fields=[
                    "jilu_id",
                ],
                name="jilu_id_idx",
            ),
        ]
        ordering = ["-updated"]


class TaskResult(models.Model):
    task = models.ForeignKey(UserTask, on_delete=models.CASCADE)
    result = models.ImageField(upload_to=upload_cs_image_result)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "task_result"
        ordering = ["-created"]
