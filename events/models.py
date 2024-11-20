from django.db import models
from userauth.models import UserProfile  # Import the custom user model
from datetime import datetime


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)
    recurrence_rule = models.JSONField(blank=True, null=True)  # Store recurrence rules here
    
    def __str__(self):
        return self.name

    def get_next_occurrences(self, limit=5):
        """
        Implement logic here to calculate the next `limit` occurrences based on `recurrence_rule`.
        You can use libraries like `rrule` for recurring rules or implement your own logic.
        """
        if not self.recurrence_rule:
            return []

        # Example logic for weekly recurrence (you can expand this based on your rules)
        from dateutil.rrule import rrulestr
        from datetime import timedelta
        
        rule = rrulestr(self.recurrence_rule)
        return list(rule[:limit])



class Registration(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # Link to UserProfile
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')  # Prevent duplicate registrations

    def __str__(self):
        return f"{self.user.username} -> {self.event.name}"
