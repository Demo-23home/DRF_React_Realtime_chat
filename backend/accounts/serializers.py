from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSeriailzer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    extra_kwargs = {"password", {"write_only": True}}

    class Meta:
        model = get_user_model()
        fields = ["email", "password", "first_name", "last_name"]

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        return user
