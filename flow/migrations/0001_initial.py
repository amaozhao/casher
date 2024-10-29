# Generated by Django 4.2.16 on 2024-10-24 08:06

import django.db.models.deletion
from django.db import migrations, models

import flow.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="WorkFlowComment",
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
                ("comment", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "workflow_comment",
                "ordering": ["-created"],
            },
        ),
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
                ("res_node", models.CharField(blank=True, max_length=100, null=True)),
                ("main_images", models.JSONField(blank=True, null=True)),
                ("title", models.CharField(max_length=255)),
                ("gn_desc", models.TextField()),
                ("sy_desc", models.TextField()),
                ("fee", models.DecimalField(decimal_places=2, max_digits=10)),
                ("free_times", models.PositiveIntegerField(default=0)),
                ("uniqueid", models.CharField(max_length=255)),
                ("client_id", models.CharField(max_length=255)),
                ("output", models.JSONField(blank=True, null=True)),
                ("workflow", models.JSONField(blank=True, null=True)),
                ("post_data", models.JSONField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "workflow_data",
                "ordering": ["-created"],
            },
        ),
        migrations.CreateModel(
            name="WorkFlowImage",
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
                ("image", models.ImageField(upload_to=flow.models.upload_image_to)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "workflow",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="flow.workflowdata",
                    ),
                ),
            ],
            options={
                "db_table": "workflow_image",
                "ordering": ["-created"],
            },
        ),
        migrations.AddIndex(
            model_name="workflowdata",
            index=models.Index(fields=["techsid"], name="techsid_idx"),
        ),
        migrations.AddIndex(
            model_name="workflowdata",
            index=models.Index(fields=["uniqueid"], name="uniqueid_idx"),
        ),
        migrations.AddIndex(
            model_name="workflowdata",
            index=models.Index(fields=["client_id"], name="client_id_idx"),
        ),
        migrations.AddField(
            model_name="workflowcomment",
            name="workflow",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="flow.workflowdata",
            ),
        ),
    ]
