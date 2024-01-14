from django.test import TestCase
from app.tests.unit.fixtures import MessageFactory, UserFactory, RoomFactory


class MessageTestCase(TestCase):
    def setUp(self):
        self.user1 = UserFactory.create()
        self.user2 = UserFactory.create()
        self.room = RoomFactory.create()
        self.message = MessageFactory.create(
            sender=self.user1,
            recipient=self.user2,
            room=self.room,
        )

    def test_send_message_success(self):
        pass
