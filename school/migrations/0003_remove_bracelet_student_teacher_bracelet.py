# Generated by Django 4.2.5 on 2024-02-25 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0002_teacher"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bracelet",
            name="student",
        ),
        migrations.AddField(
            model_name="teacher",
            name="bracelet",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.RESTRICT,
                to="school.bracelet",
            ),
        ),
    ]
