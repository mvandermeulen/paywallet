# Generated by Django 4.2.5 on 2024-03-02 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Bracelet",
            fields=[
                (
                    "rfid",
                    models.CharField(
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="RFID",
                    ),
                ),
                (
                    "model_name",
                    models.CharField(max_length=100, verbose_name="Bracelet Model"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("assigned", "Assigned"),
                            ("unassigned", "Unassigned"),
                        ],
                        default="unassigned",
                        max_length=100,
                        verbose_name="Status",
                    ),
                ),
            ],
            options={
                "verbose_name": "Bracelet",
                "verbose_name_plural": "Bracelets",
            },
        ),
        migrations.CreateModel(
            name="School",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                ("address", models.CharField(max_length=100, verbose_name="Address")),
                ("city", models.CharField(max_length=100, verbose_name="City")),
                (
                    "phone_number",
                    models.CharField(max_length=100, verbose_name="Phone Number"),
                ),
                (
                    "primary_email",
                    models.CharField(max_length=100, verbose_name="Primary Email"),
                ),
                (
                    "school_admin",
                    models.ForeignKey(
                        limit_choices_to={"groups__name": "School Admin"},
                        on_delete=django.db.models.deletion.RESTRICT,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="School Admin",
                    ),
                ),
            ],
            options={
                "verbose_name": "School",
                "verbose_name_plural": "Schools",
            },
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "first_name",
                    models.CharField(max_length=100, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=100, verbose_name="Last Name"),
                ),
                (
                    "registration_number",
                    models.CharField(
                        max_length=100, verbose_name="Registration Number"
                    ),
                ),
                ("grade", models.IntegerField(default=0, verbose_name="Grade")),
                (
                    "date_of_birth",
                    models.DateField(default=None, verbose_name="Date of Birth"),
                ),
                (
                    "bracelet",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="school.bracelet",
                        unique=True,
                        verbose_name="Bracelet",
                    ),
                ),
                (
                    "school",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="school.school",
                        verbose_name="School",
                    ),
                ),
            ],
            options={
                "verbose_name": "Student",
                "verbose_name_plural": "Students",
                "unique_together": {("registration_number", "school")},
            },
        ),
        migrations.AddField(
            model_name="bracelet",
            name="school",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="school.school",
                verbose_name="School",
            ),
        ),
        migrations.CreateModel(
            name="Attendance",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("in_time", models.DateTimeField(auto_now_add=True)),
                ("out_time", models.DateTimeField(blank=True, default=None, null=True)),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="school.student",
                    ),
                ),
            ],
            options={
                "verbose_name": "Attendance",
                "verbose_name_plural": "Attendance",
            },
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "first_name",
                    models.CharField(max_length=100, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=100, verbose_name="Last Name"),
                ),
                (
                    "registration_number",
                    models.CharField(
                        max_length=100, verbose_name="Registration Number"
                    ),
                ),
                ("grade", models.IntegerField(default=0, verbose_name="Grade")),
                (
                    "bracelet",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="school.bracelet",
                    ),
                ),
                (
                    "school",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="school.school",
                        verbose_name="School",
                    ),
                ),
            ],
            options={
                "verbose_name": "Teacher",
                "verbose_name_plural": "Teachers",
                "unique_together": {("registration_number", "school")},
            },
        ),
        migrations.AlterUniqueTogether(
            name="bracelet",
            unique_together={("rfid", "school")},
        ),
    ]
