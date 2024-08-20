from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from user.models import UserAccount
from ..serializers.register import UserRegistrationSerializer
from ..serializers.user_list import UserListSerializer


class UserAddOrListView(APIView):
    """
    -Authenticated Users can add new users account by email, frist_name, last_name and password.
    -Possible to add multiple user at a time
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status.HTTP_201_CREATED)

        return Response(status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        users = UserAccount.objects.filter(is_active=True)
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)
