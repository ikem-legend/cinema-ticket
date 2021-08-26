from rest_framework import serializers
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "user_id",
            "date_of_birth",
            "date_created",
            "is_staff",
            "is_active",
            "is_verified",
        )
