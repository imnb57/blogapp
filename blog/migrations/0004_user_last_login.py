# Generated by Django 5.1.7 on 2025-03-19 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_user_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
    ]
