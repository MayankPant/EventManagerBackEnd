from datetime import timedelta, date
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Event
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import EventSerializer
from rest_framework.views import APIView
from .utils import generate_recurrences



@api_view(['GET'])
def get_event_occurrences(request, event_id):
    event = Event.objects.get(id=event_id)
    occurrences = generate_recurrences(event)
    return Response(occurrences)

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically assign the event to the logged-in user
        serializer.save(created_by=self.request.user)

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        event = super().get_object()
        if event.created_by != self.request.user:
            raise PermissionDenied("You do not have permission to modify this event.")
        return event


class EventRecurrenceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            event = Event.objects.get(pk=pk, created_by=request.user)
            next_occurrences = event.get_next_occurrences()
            return Response({'next_occurrences': next_occurrences})
        except Event.DoesNotExist:
            return Response({'detail': 'Event not found or you do not have permission to access it.'}, status=404)