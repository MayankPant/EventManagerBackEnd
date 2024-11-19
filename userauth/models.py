from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    # Extend Django's User model
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Optional
    is_admin = models.BooleanField(default=False)  # Admin privileges

    def __str__(self):
        return self.username
