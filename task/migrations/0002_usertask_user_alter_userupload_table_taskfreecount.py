# Generated by Django 4.2.16 on 2024-11-05 03:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("flow", "0001_initial"),
        ("task", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="usertask",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterModelTable(
            name="userupload",
            table="user_task_upload",
        ),
        migrations.CreateModel(
            name="TaskFreeCount",
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
                ("free_count", models.IntegerField(default=0)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "workflow",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="task_count",
                        to="flow.workflowdata",
                    ),
                ),
            ],
            options={
                "db_table": "task_free_count",
            },
        ),
    ]
