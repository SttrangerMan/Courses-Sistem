# Generated by Django 5.0.6 on 2024-05-23 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0003_alter_content_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
