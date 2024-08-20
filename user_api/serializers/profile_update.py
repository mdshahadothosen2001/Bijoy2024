from rest_framework.serializers import ModelSerializer

from user.models import UserAccount


class UpdateProfileSerializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = [
            "first_name",
            "last_name",
        ]
