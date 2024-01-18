from django.views.generic import TemplateView
from app.models import Message


class ChatView(TemplateView):
    template_name = "chat.html"

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["messages"] = Message.objects.all()
        return kwargs
