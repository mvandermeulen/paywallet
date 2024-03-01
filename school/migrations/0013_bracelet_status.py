# Generated by Django 4.2.5 on 2024-03-01 17:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0012_remove_student_bracelet_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="bracelet",
            name="status",
            field=models.CharField(
                choices=[
                    ("assigned", "Assigned"),
                    ("inactive", "Inactive"),
                    ("unassigned", "Unassigned"),
                ],
                default="unassigned",
                max_length=100,
                verbose_name="Status",
            ),
        ),
    ]
