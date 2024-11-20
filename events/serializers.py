from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'location', 'start_time', 'end_time', 'created_by', 'recurrence_rule']
        read_only_fields = ['id', 'created_by']
        
    def create(self, validated_data):
        # You can add logic to handle the recurrence rule here, if necessary
        event = Event.objects.create(**validated_data)
        return event
