import hashlib


def generate_subject_id(study_id, study_subject_id):
    return hashlib.sha256(
        (study_id + study_subject_id).encode('utf-8')
    ).hexdigest()
