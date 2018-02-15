from django.urls import re_path

from . import views

app_name = 'id_generator'
urlpatterns = [
    re_path(r'^$', views.generate_miro_subject_id, name="generate"),
]
