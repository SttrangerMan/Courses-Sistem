from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Course
from students_courses.serializer import StudentsSerializer
from accounts.models import Account


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses",
        ]
        extra_kwargs = {
            "status": {"read_only": True},
            "contents": {"read_only": True},
            "students_courses": {"read_only": True},
        }


class CourseStudentSerializer(ModelSerializer):
    students_courses = StudentsSerializer(many=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "students_courses",
        ]
        read_only_fields = ["id", "name"]

    def update(self, instance, validated_data):
        students = []
        not_students = []

        for students_courses in validated_data["students_courses"]:
            student_email = students_courses["student"]["email"]
            student = Account.objects.filter(email=student_email).first()

            if not student:
                not_students.append(student_email)
            else:
                students.append(student)
        if len(not_students):
            message = ", ".join(not_students)
            raise ValidationError(
                {"detail": f"No active accounts was found: {message}."}
            )
        instance.students.add(*students)
        return instance
