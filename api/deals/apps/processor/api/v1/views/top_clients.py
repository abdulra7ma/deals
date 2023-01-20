from rest_framework.views import APIView

from ....services.top_clients import TopClientsService


class TopClientsView(APIView):
    def get(self, request, *args, **kwargs):
        response = TopClientsService().top_clients()
        return response
