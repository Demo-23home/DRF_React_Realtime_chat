import jwt
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta

from accounts.models import User


class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token = self.extract_token(request=request)
        if token == None:
            return None
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithm=["HS256"])
            self.verify_token(payload=payload)

            user_id = payload["id"]
            user = User.objects.get(id=user_id)

        except (InvalidTokenError, ExpiredSignatureError, User.DoesNotExist):
            raise AuthenticationFailed("Invalid Token")

    def verify_token(self, payload):
        if "exp" not in payload:
            raise InvalidTokenError("Token has no expiration")

        exp = payload["exp"]
        now_time = datetime.now().timestamp()

        if now_time >= exp:
            raise InvalidTokenError("Token has expired")

    def extract_token(self, request):
        auth_headers = request.headers.get("Authorization")
        if auth_headers and auth_headers.startswith("Bearer "):
            return auth_headers.split(" ")[1]
        return None

    def generate_token(payload):
        expire_date = datetime.now() + timedelta(hours=24)
        payload["exp"] = expire_date

        token = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm="HS256")
        return token
