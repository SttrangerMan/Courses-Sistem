from django.urls import path
from .views import (
    courseUpdateAndDestroyDetailsViews,
    courseCreateAndListViews,
    courseUpdateAndPutDetailsViews,
)

urlpatterns = [
    path("courses/", courseCreateAndListViews.as_view()),
    path("courses/<course_id>/", courseUpdateAndDestroyDetailsViews.as_view()),
    path("courses/<course_id>/students/", courseUpdateAndPutDetailsViews.as_view()),
]
