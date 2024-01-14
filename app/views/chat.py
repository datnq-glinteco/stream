from django.views.generic import TemplateView


class ChatView(TemplateView):
    template_name = ""

    def get_queryset(self):
        return super().get_queryset()
