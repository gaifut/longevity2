from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "CustomUserSerializer"
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name'
        )
