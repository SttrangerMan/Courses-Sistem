from .serializer import CourseSerializer, CourseStudentSerializer
from rest_framework import generics
from .models import Course
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import MyCustonPermission, StudentPermission


class courseCreateAndListViews(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustonPermission]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset.all()
        return self.queryset.filter(students=self.request.user)


class courseUpdateAndDestroyDetailsViews(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [StudentPermission]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_url_kwarg = "course_id"


class courseUpdateAndPutDetailsViews(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustonPermission]
    queryset = Course.objects.all()
    serializer_class = CourseStudentSerializer
    lookup_url_kwarg = "course_id"
