import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Account(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="account_users",
        blank=True,
        help_text=(
            "The groups this user belongs to. A user will get all permissions granted to each of their groups."
        ),
        related_query_name="account",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="account_users",
        blank=True,
        help_text=("Specific permissions for this user."),
        related_query_name="account",
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=100, unique=True)
    is_superuser = models.BooleanField(default=False)
