import os

from django.contrib.auth.models import User
from django.db import models


def upload_image_to(instance, filename):
    """
    自定义上传路径，根据 techsid 动态设置目录，防止文件名冲突
    """
    # 根据 techsid 创建目录
    upload_dir = f"user/images/"
    return os.path.join(upload_dir, filename)


class WorkFlowData(models.Model):
    techsid = models.CharField(max_length=100)  # 保存 techsid
    res_node = models.CharField(max_length=100, blank=True, null=True)
    main_images = models.JSONField(
        null=True, blank=True
    )  # 主要的图片信息可以作为JSON保存
    title = models.CharField(max_length=255)  # 作品标题
    gn_desc = models.TextField()  # 作品功能介绍
    sy_desc = models.TextField()  # 作品使用说明
    fee = models.DecimalField(max_digits=10, decimal_places=2)  # 费用
    free_times = models.PositiveIntegerField(default=0)  # 免费使用次数
    uniqueid = models.CharField(max_length=255)  # 唯一标识符
    client_id = models.CharField(max_length=255)  # 唯一标识符
    output = models.JSONField(null=True, blank=True)  # 保存原始输出数据
    workflow = models.JSONField(null=True, blank=True)  # 保存工作流数据
    post_data = models.JSONField(null=False)  # 保存提交的postData
    status = models.CharField(max_length=10, default='online')
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "workflow_data"
        indexes = [
            models.Index(
                fields=[
                    "techsid",
                ],
                name="techsid_idx",
            ),
            models.Index(
                fields=[
                    "uniqueid",
                ],
                name="uniqueid_idx",
            ),
            models.Index(
                fields=[
                    "client_id",
                ],
                name="client_id_idx",
            ),
        ]
        ordering = ["-created"]


class WorkFlowImage(models.Model):
    workflow = models.ForeignKey(
        WorkFlowData, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to=upload_image_to)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "workflow_image"
        ordering = ["-created"]


class WorkFlowComment(models.Model):
    workflow = models.ForeignKey(
        WorkFlowData, related_name="comments", on_delete=models.CASCADE
    )
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "workflow_comment"
        ordering = ["-created"]


class WorkFlowBanner(models.Model):
    workflow = models.ForeignKey(WorkFlowData, on_delete=models.CASCADE)
    is_visible = models.BooleanField(default=True)
    desc = models.TextField()
    url = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "workflow_banner"
        ordering = ["-created"]
