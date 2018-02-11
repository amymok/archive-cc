from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from id_generator.serializers import MiroSubjectIdInput
from id_generator.id_generator import generate_subject_id

@api_view(['GET'])
def generate_miro_subject_id(request):
    """
    Generate a Miro Subject ID based on Study ID and Study Subject ID
    """
    id_input = MiroSubjectIdInput(data=request.query_params)

    if not id_input.is_valid():
        return Response(
            id_input.errors, status=status.HTTP_400_BAD_REQUEST
        )

    unique_id = generate_subject_id(
        id_input.validated_data["study_id"],
        id_input.validated_data["study_subject_id"]
    )
    return Response({
        "miro_subject_id": "{}".format(unique_id)
    })