# Generated by Django 4.2.16 on 2024-11-12 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("task_manager", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="assigned_to",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="assigned_tasks",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
