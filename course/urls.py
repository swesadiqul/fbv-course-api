from django.urls import path
from .views import *

urlpatterns = [
    path('course', course_api, name='course'),
    path('course_details/<int:pk>', course_details, name='course_details'),
]
