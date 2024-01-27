from typing import Any
import uuid
from django.db import models
from django.contrib.auth.models import User, Group
from school.models import Student


class Guardian(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True, blank=True, default=None)
    device_fcm_token = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
