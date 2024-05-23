from django.urls import path
from .views import ContentCreatViews, ContentUpdateAndDestroyViews

urlpatterns = [
    path("courses/<course_id>/contents/", ContentCreatViews.as_view()),
    path(
        "courses/<course_id>/contents/<content_id>/",
        ContentUpdateAndDestroyViews.as_view(),
    ),
]
