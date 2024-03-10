# Generated by Django 4.2.5 on 2024-03-10 03:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("school", "0009_operator"),
    ]

    operations = [
        migrations.CreateModel(
            name="SchoolAdministrator",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("phone", models.CharField(max_length=20)),
                (
                    "school",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="school.school"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "School Administrator",
                "verbose_name_plural": "School Administrators",
            },
        ),
    ]
