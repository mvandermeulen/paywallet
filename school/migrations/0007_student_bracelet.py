# Generated by Django 4.2.5 on 2024-02-25 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0006_remove_student_bracelet"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="bracelet",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="school.bracelet",
                verbose_name="Bracelet",
            ),
        ),
    ]
