from django.test import TestCase
from app.tests.unit.fixtures import MessageFactory, UserFactory, RoomFactory
from django.test import Client


class MessageTestCase(TestCase):
    def setUp(self):
        self.user1 = UserFactory.create()
        self.user2 = UserFactory.create()
        self.room = RoomFactory.create()
        MessageFactory.create(
            sender=self.user1,
            recipient=self.user2,
            room=self.room,
        )
        MessageFactory.create(
            sender=self.user2,
            recipient=self.user2,
            room=self.room,
        )
        self.client = Client()

    def test_get_success(self):
        response = self.client.get("/chat/")
        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(response.context.get("messages")))
