import factory
from app.models import Message
from .user import UserFactory
from .room import RoomFactory


class MessageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Message

    sender = factory.SubFactory(UserFactory)
    recipient = factory.SubFactory(UserFactory)
    room = factory.SubFactory(RoomFactory)
    content = "This is message"
