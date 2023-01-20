from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView

from ....services.client import ClientService


class UploadCSV(APIView):
    parser_classes = [MultiPartParser]

    @swagger_auto_schema(
        operation_description="Upload file...",
        manual_parameters=[
            openapi.Parameter(
                "file",
                openapi.IN_FORM,
                type=openapi.TYPE_FILE,
                description="CSV to be uploaded"
            )
        ],
    )
    def post(self, request, *args, **kwargs):
        response = ClientService().load_csv(request)
        return response
