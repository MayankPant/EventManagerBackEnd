"""
Generates occurences based on events

"""
from datetime import timedelta
from .models import Event

def generate_recurrences(event):
    occurrences = []
    if event.is_recurring:
        current_date = event.start_time.date()
        while current_date <= event.recurrence_end_date:
            occurrences.append({
                "name": event.name,
                "start_time": current_date.isoformat(),
                "location": event.location
            })
            if event.recurrence_pattern == Event.DAILY:
                current_date += timedelta(days=1)
            elif event.recurrence_pattern == Event.WEEKLY:
                current_date += timedelta(weeks=1)
            elif event.recurrence_pattern == Event.MONTHLY:
                current_date = current_date.replace(month=current_date.month + 1)
            elif event.recurrence_pattern == Event.YEARLY:
                current_date = current_date.replace(year=current_date.year + 1)
    return occurrences