# Generated by Django 4.2.5 on 2024-03-01 17:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0009_alter_student_bracelet"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="bracelet_status",
            field=models.BooleanField(default=True, verbose_name="Bracelet Status"),
        ),
    ]