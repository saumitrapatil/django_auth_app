from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class User(AbstractUser):
    last_updated = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        self.last_updated = now()
        super().save(*args, **kwargs)