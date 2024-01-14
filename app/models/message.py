from django.db import models
from django.contrib.auth.models import User
from .room import Room


class Message(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages"
    )
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipient"
    )
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="room"
    )
    content = models.CharField(max_length=250, default="")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
