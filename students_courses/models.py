import uuid
from django.db import models
from accounts.models import Account
from courses.models import Course


class STUDENT_COURSE_STATUS(models.TextChoices):
    pending = "pending"
    accepted = "accepted"


class StudentCourse(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    status = models.CharField(
        max_length=20,
        choices=STUDENT_COURSE_STATUS.choices,
        default=STUDENT_COURSE_STATUS.pending,
    )
    student = models.ForeignKey(
        Account, related_name="students_courses", on_delete=models.CASCADE, default=None
    )
    course = models.ForeignKey(
        Course, related_name="students_courses", on_delete=models.CASCADE, default=None
    )
