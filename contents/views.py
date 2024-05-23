from .serializer import ContentSerializer
from .models import Content
from rest_framework import generics, exceptions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import MyCustonPermission, StudentPermission
from courses.models import Course
from rest_framework.permissions import IsAuthenticated


class ContentCreatViews(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, MyCustonPermission]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "course_id"

    def perform_create(self, serializer):
        course = Course.objects.get(id=self.kwargs["course_id"])
        if not course:
            raise exceptions.NotFound({"detail": "course not found"})
        serializer.save(course=course)


class ContentUpdateAndDestroyViews(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [StudentPermission]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "content_id"

    def get_object(self):
        course = Course.objects.filter(id=self.kwargs["course_id"]).first()
        content = Content.objects.filter(id=self.kwargs["content_id"]).first()

        if not course:
            raise exceptions.NotFound({"detail": "course not found."})
        if not content:
            raise exceptions.NotFound({"detail": "content not found."})
        self.check_object_permissions(self.request, content)
        return content
