from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from accounts.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_all_users(request):
    try:
        users = User.objects.exclude(id=request.user.id)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    except Exception as e:
        print({"Error listing users": str(e)})
        return Response({"Error listing users": str(e)}, status=400)
