# Generated by Django 5.0.6 on 2024-05-18 04:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('courses', '0002_course_instructor_course_students'),
        ('students_courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcourse',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='students_courses', to='courses.course'),
        ),
        migrations.AddField(
            model_name='studentcourse',
            name='student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='students_courses', to='accounts.account'),
        ),
    ]
