# Generated by Django 5.0.6 on 2024-05-23 00:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0005_alter_content_name'),
        ('courses', '0002_course_instructor_course_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='courses.course'),
        ),
    ]
