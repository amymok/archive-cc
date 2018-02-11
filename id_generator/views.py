from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def generate_miro_subject_id(request):
    """
    Generate a Miro Subject ID based on Study ID and Study Subject ID
    """
    return Response({"miro_subject_id": "1234AE3"})