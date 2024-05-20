from rest_framework.serializers import ModelSerializer
from .models import Account


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "password",
            "email",
            "is_superuser",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_superuser": {"default": False},
        }

    def create(self, validated_data: dict):
        return Account.objects.create_user(**validated_data)
