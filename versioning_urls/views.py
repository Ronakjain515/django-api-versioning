from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import URLPathVersioningClassSerializer, AcceptHeaderVersioningClassSerializer
from versioning.VersioningClass import URLPathVersioningClass, AcceptHeaderVersioningClass, QueryParameterVersioningClass, HostNameVersioningClass


# Create your views here.
class URLPathVersioningClassAPIView(APIView):
    serializer_class = URLPathVersioningClassSerializer
    versioning_class = URLPathVersioningClass

    def get(self, request, *args, **kwargs):
        data = {
            'field1': 'Dummy Value 1',
            'field2': 'Dummy Value 2',
            'field3': 'Dummy Value 3',
        }

        # Initialize the serializer with data
        serializer = URLPathVersioningClassSerializer(context={'request': request},data=data)
        serializer.is_valid(raise_exception=True)  # Validate the serializer data

        # Retrieve serialized data
        serialized_data = serializer.data
        # Prepare response format
        response_format = {
            "status_code": 200,
            "error": None,
            "data": serialized_data,
            "message": 'Success'
        }

        return Response(response_format)


class AcceptHeaderVersioningClassAPIView(APIView):
    media_type = 'application/vnd.megacorp.bookings+json'   
    serializer_class = URLPathVersioningClassSerializer
    versioning_class = AcceptHeaderVersioningClass

    def get(self, request, *args, **kwargs):
        data = {
            'field1': 'Dummy Value 1',
            'field2': 'Dummy Value 2',
            'field3': 'Dummy Value 3',
        }

        # Initialize the serializer with data
        serializer = AcceptHeaderVersioningClassSerializer(context={'request': request},data=data)
        serializer.is_valid(raise_exception=True)  # Validate the serializer data

        # Retrieve serialized data
        serialized_data = serializer.data
        # Prepare response format
        response_format = {
            "status_code": 200,
            "error": None,
            "data": serialized_data,
            "message": 'Success'
        }

        return Response(response_format)

class QueryParamterVersioningClassAPIView(APIView):
    versioning_class = QueryParameterVersioningClass
    def get(self, request, *args, **kwargs):

        # Prepare response format
        response_format = {
            "status_code": 200,
            "error": None,
            "data": request.query_params.get('version'),
            "message": 'Success'
        }

        return Response(response_format)


class HostNameVersioningClassAPIView(APIView):
    versioning_class = HostNameVersioningClass
    def get(self, request, *args, **kwargs):
        print(request.version)
        # Prepare response format
        response_format = {
            "status_code": 200,
            "error": None,
            "data": request.query_params.get('version'),
            "message": 'Success'
        }

        return Response(response_format)