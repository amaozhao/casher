# Generated by Django 4.2.16 on 2024-11-06 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("flow", "0002_workflowbanner"),
    ]

    operations = [
        migrations.RenameField(
            model_name="workflowbanner",
            old_name="en_desc",
            new_name="url",
        ),
    ]