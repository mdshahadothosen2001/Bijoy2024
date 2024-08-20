from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.register import UserRegistrationSerializer
from ..serializers.token import CustomTokenObtainPairSerializer


class UserRegistrationView(APIView):
    """Users can register their account by email, frist_name, last_name and password."""

    permission_classes = [AllowAny]

    def validate_parameter(self, email, password):
        if email and password:
            return True
        else:
            return False

    def post(self, request):
        email = request.data.get("email")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        password = request.data.get("password")

        if self.validate_parameter(email, password) is True:
            user_data = {
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "password": password,
            }

            serializer = UserRegistrationSerializer(data=user_data)
            if serializer.is_valid():
                user = serializer.save()

                token_serializer = CustomTokenObtainPairSerializer()
                tokens = token_serializer.get_token(user)

                return Response({
                    "access": str(tokens.access_token),
                    "refresh": str(tokens),
                })

        return Response("Incompleted registration! Please provide valid data")
