from django.urls import path
from .views import EventListCreateView, EventDetailView, EventRecurrenceView

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('events/<int:pk>/recurrence/', EventRecurrenceView.as_view(), name='event-recurrence'),
]
