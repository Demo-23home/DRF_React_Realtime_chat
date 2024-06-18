from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer


@api_view(["POST"])
def register(request):
    data = request.data
    serializer = RegisterSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
