# Generated by Django 5.1.2 on 2024-10-17 08:43

import django.db.models.deletion
import flow.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkFlowData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("techsid", models.CharField(max_length=100)),
                ("client_id", models.CharField(blank=True, max_length=100, null=True)),
                ("res_node", models.CharField(blank=True, max_length=100, null=True)),
                ("main_images", models.JSONField(blank=True, null=True)),
                ("title", models.CharField(max_length=255)),
                ("gn_desc", models.TextField()),
                ("sy_desc", models.TextField()),
                ("fee", models.DecimalField(decimal_places=2, max_digits=10)),
                ("free_times", models.PositiveIntegerField(default=0)),
                ("uniqueid", models.CharField(max_length=255, unique=True)),
                ("output", models.JSONField(blank=True, null=True)),
                ("workflow", models.JSONField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["-created"],
            },
        ),
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VideoNode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("video", models.FileField(upload_to=flow.models.upload_video_to)),
                ("desc", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "post_data",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cs_video_nodes",
                        to="flow.workflowdata",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ImageNode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.FileField(upload_to=flow.models.upload_image_to)),
                ("desc", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "post_data",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cs_img_nodes",
                        to="flow.workflowdata",
                    ),
                ),
            ],
        ),
    ]
