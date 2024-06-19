# from rest_framework import serializers
# from django.contrib.auth import get_user_model, authenticate

# from .token_authentication import JWTAuthentication

# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     extra_kwargs = {"password": {"write_only": True}}

#     class Meta:
#         model = get_user_model()
#         fields = ["email", "password", "first_name", "last_name"]

#     def create(self, validated_data):
#         user = get_user_model().objects.create_user(
#             email=validated_data["email"],
#             password=validated_data["password"],
#             first_name=validated_data["first_name"],
#             last_name=validated_data["last_name"],
#         )
#         return user


# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, data):
#         email = data.get("email")
#         password = data.get("password")
#         user = authenticate(username=email, password=password)

#         if user and user.is_active:
#             payload = {
#                 "user_id": user.id,
#                 "email": user.email,
#             }
#             token = JWTAuthentication.generate_token(payload)
#             data = {"id": user.id, "email": user.email, "token": token}
#             return data
#         else:
#             raise serializers.ValidationError("Incorrect email or password")


from rest_framework_simplejwt.tokens import Token
from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = ["id", "email"]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["email"] = user.email

        return token


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "email",
            "password",
        ]

    def create(self, validated_data):
        user = User.objects.create(email=validated_data["email"])

        user.set_password(validated_data["password"])
        user.save()

        return user
