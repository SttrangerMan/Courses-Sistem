import uuid
from django.db import models
from accounts.models import Account


class CourseStatus(models.TextChoices):
    not_started = "not started"
    in_progress = "in progress"
    finished = "finished"


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=11, choices=CourseStatus.choices, default=CourseStatus.not_started
    )
    start_date = models.DateField()
    end_date = models.DateField()

    instructor = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name="courses",
        null=True,
        default=None,
    )

    students = models.ManyToManyField(
        Account,
        related_name="my_courses",
        through="students_courses.StudentCourse",
        default=None,
    )
