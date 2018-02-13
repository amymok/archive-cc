from django.urls import re_path
import id_generator.views

app_name = 'id_generator'
urlpatterns = [
    re_path(r'^$', id_generator.views.generate_miro_subject_id, name="generate"),
]
