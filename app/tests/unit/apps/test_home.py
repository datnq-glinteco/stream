from django.test import TestCase
from app.tests.unit.fixtures import MessageFactory, UserFactory, RoomFactory
from django.test import Client
from django.urls import reverse_lazy


class HomeTestCase(TestCase):
    def setUp(self):
        self.user1 = UserFactory.create()

    def test_get_success(self):
        response = self.client.get("/home/")
        self.assertEqual(200, response.status_code)
