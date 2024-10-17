import os
from django.contrib.auth.models import User
from django.db import models



def upload_image_to(instance, filename):
    """
    自定义上传路径，根据 techsid 动态设置目录，防止文件名冲突
    """
    # 根据 techsid 创建目录
    upload_dir = f'workflow/images/{instance.techsid}'
    return os.path.join(upload_dir, filename)


def upload_video_to(instance, filename):
    """
    自定义上传路径，根据 techsid 动态设置目录，防止文件名冲突
    """
    # 根据 techsid 创建目录
    upload_dir = f'workflow/videos/{instance.techsid}'
    return os.path.join(upload_dir, filename)


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class WorkFlowData(models.Model):
    techsid = models.CharField(max_length=100)  # 保存 techsid
    client_id = models.CharField(max_length=100, blank=True, null=True)  # 保存 client_id
    res_node = models.CharField(max_length=100, blank=True, null=True)
    main_images = models.JSONField(null=True, blank=True)  # 主要的图片信息可以作为JSON保存
    title = models.CharField(max_length=255)  # 作品标题
    gn_desc = models.TextField()  # 作品功能介绍
    sy_desc = models.TextField()  # 作品使用说明
    fee = models.DecimalField(max_digits=10, decimal_places=2)  # 费用
    free_times = models.PositiveIntegerField(default=0)  # 免费使用次数
    uniqueid = models.CharField(max_length=255, unique=True)  # 唯一标识符
    output = models.JSONField(null=True, blank=True)  # 保存原始输出数据
    workflow = models.JSONField(null=True, blank=True)  # 保存工作流数据
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]


class ImageNode(models.Model):
    """
    保存自定义图片节点的信息
    """
    post_data = models.ForeignKey(WorkFlowData, related_name="cs_img_nodes", on_delete=models.CASCADE)
    image = models.FileField(upload_to=upload_image_to)  # 图片上传字段
    desc = models.CharField(max_length=255, blank=True, null=True)  # 图片描述

    def __str__(self):
        return f"ImageNode for PostData {self.post_data.uniqueid}"

class VideoNode(models.Model):
    """
    保存自定义视频节点的信息
    """
    post_data = models.ForeignKey(WorkFlowData, related_name="cs_video_nodes", on_delete=models.CASCADE)
    video = models.FileField(upload_to=upload_video_to)  # 视频上传字段
    desc = models.CharField(max_length=255, blank=True, null=True)  # 视频描述

    def __str__(self):
        return f"VideoNode for PostData {self.post_data.uniqueid}"
