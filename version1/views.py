from rest_framework.views import APIView
from rest_framework.response import Response

from versioning.VersioningClass import NameSpaceVersioningClass


# Create your views here.
class Version1ClassAPIView(APIView):
    media_type = 'application/vnd.megacorp.bookings+json'
    versioning_class = NameSpaceVersioningClass

    def get(self, request, *args, **kwargs):

        # Prepare response format
        response_format = {
            "status_code": 200,
            "error": None,
            "data": "Version 1",
            "message": 'Success'
        }

        return Response(response_format)

