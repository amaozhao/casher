# Generated by Django 4.2.16 on 2024-11-10 03:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("wxappb", "0002_wxappbtechs_provider"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="WxAppBTechs",
            new_name="AuthorTechs",
        ),
    ]
