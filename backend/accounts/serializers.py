from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    extra_kwargs = {"password": {"write_only": True}}

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


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    id = serializers.IntegerField(read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)

        if email and password:
            user = authenticate(username=email, password=password)

            if user:
                data["user"] = user
            else:
                raise serializers.ValidationError("Incorrect email or password")
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'")

        if not user.is_active:
            serializers.ValidationError("User is Inactive")

        data = {"id": user.id, "email": email}
        return data
