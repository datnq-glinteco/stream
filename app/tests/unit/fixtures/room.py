import factory
from app.models import Room


class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Room
