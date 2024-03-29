from rest_framework.viewsets import ModelViewSet
from app.models import Message
from api.serializers import MessageSerializer


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
