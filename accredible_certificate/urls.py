from django.urls import re_path
from .views import request_certificate
from .views import update_certificate


urlpatterns = [
    re_path(r'^request_certificate$', request_certificate, name='request_certificate'),
    re_path(r'^update_certificate$', update_certificate, name='update_certificate')
]
