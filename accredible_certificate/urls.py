from django.urls import path
from . import views

urlpatterns = [
    path('request_certificate', views.request_certificate, name='request_certificate'),
    path('update_certificate', views.update_certificate, name='update_certificate'),
]