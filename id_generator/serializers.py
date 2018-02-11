from rest_framework import serializers

class MiroSubjectIdInput(serializers.Serializer):
    study_id = serializers.CharField(required=True)
    study_subject_id = serializers.CharField(required=True)
