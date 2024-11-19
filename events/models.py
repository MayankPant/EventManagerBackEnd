from django.db import models
from userauth.models import UserProfile  # Import the custom user model

class Event(models.Model):
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    YEARLY = 'yearly'

    RECURRENCE_CHOICES = [
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
        (MONTHLY, 'Monthly'),
        (YEARLY, 'Yearly'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    capacity = models.PositiveIntegerField()
    is_recurring = models.BooleanField(default=False)
    recurrence_pattern = models.CharField(
        max_length=20,
        choices=RECURRENCE_CHOICES,
        blank=True,
        null=True
    )
    recurrence_end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




class Registration(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # Link to UserProfile
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')  # Prevent duplicate registrations

    def __str__(self):
        return f"{self.user.username} -> {self.event.name}"
