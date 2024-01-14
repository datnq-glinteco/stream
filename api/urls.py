from rest_framework.routers import DefaultRouter
from .views import MessageViewSet

app_name = "api"
router = DefaultRouter()
router.register("messages", viewset=MessageViewSet, basename="messages")

urlpatterns = []
urlpatterns += router.urls
