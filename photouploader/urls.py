from django.urls import path
from .views import request_image

urlpatterns = [
    path('',request_image,name="image-request")
]