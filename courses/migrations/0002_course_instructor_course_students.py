# Generated by Django 5.0.6 on 2024-05-18 04:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('courses', '0001_initial'),
        ('students_courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='courses', to='accounts.account'),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(default=None, related_name='my_courses', through='students_courses.StudentCourse', to='accounts.account'),
        ),
    ]