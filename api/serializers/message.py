from rest_framework import serializers
from app.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            "sender",
            "recipient",
            "room",
            "content",
            "created_at",
            "updated_at",
        ]
