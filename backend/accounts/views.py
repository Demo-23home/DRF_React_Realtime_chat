from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer, LoginSerializer
from .token_authentication import JWTAuthentication
from rest_framework import status


@api_view(["POST"])
def register(request):
    data = request.data
    serializer = RegisterSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data["user"]
        token = JWTAuthentication.generate_token({"id": user.id, "email": user.email})
        data = {"message": "Login successful", "token": token, "user": serializer.data}
        return Response(data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)