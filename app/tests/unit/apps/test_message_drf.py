from rest_framework.test import APITestCase
from unittest.mock import patch
from rest_framework.response import Response


class MessageAPITestCase(APITestCase):
    @patch("api.views.MessageViewSet.list")
    def test_api_list_message(self, mock_list):
        mock_list.return_value = Response(
            {"field1": "mocked_value", "field2": 99}
        )

        # Gọi API endpoint
        response = self.client.get("/api/messages/")

        # Kiểm tra xem giả mạo đã được gọi đúng cách chưa
        mock_list.assert_called_once()

        # Kiểm tra kết quả của API endpoint
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data, {"field1": "mocked_value", "field2": 99}
        )
