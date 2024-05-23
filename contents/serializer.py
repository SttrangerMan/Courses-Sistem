from rest_framework.serializers import ModelSerializer
from .models import Content


class ContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = [
            "id",
            "name",
            "content",
            "video_url",
        ]
        extra_kwargs = {
            "course": {"read_only": True},
            "students": {"read_only": True},
            "video_url": {"default": None},
        }
        depth = 1
