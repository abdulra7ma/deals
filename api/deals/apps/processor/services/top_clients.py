from rest_framework import status
from rest_framework.response import Response

from ..api.v1.serializers.client import ClientSerializer
from ..selectors import get_top_clients
from django.core.cache import cache


class TopClientsService:
    @staticmethod
    def top_clients():
        # Check if the top clients are already in the cache
        cached_top_clients = cache.get("top_clients")

        if cached_top_clients:
            data = cached_top_clients
        else:
            top_clients = get_top_clients()
            serializer = ClientSerializer(top_clients, many=True)
            data = serializer.data

            # set the cache for 30 minutes
            cache.set("top_clients", data, 1800)

        return Response(
            data=data,
            status=status.HTTP_200_OK,
        )
