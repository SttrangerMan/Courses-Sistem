from rest_framework import serializers
from .models import StudentCourse


class StudentsSerializer(serializers.ModelSerializer):
    student_id = serializers.CharField(source="student.id", read_only=True)
    student_username = serializers.CharField(source="student.username", read_only=True)
    student_email = serializers.CharField(source="student.email")

    class Meta:
        model = StudentCourse
        fields = [
            "id",
            "student_id",
            "student_username",
            "student_email",
            "status",
        ]
