from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..token_validation import tokenValidation
from ..serializers.profile_update import UpdateProfileSerializer
from user.models import UserAccount


class UserProfileUpdateOrDeleteView(APIView):
    """User can update their profile information"""

    permission_classes = [IsAuthenticated]

    def patch(self, request):
        payload = tokenValidation(request)
        email = payload.get("email")

        if email:
            instance = get_object_or_404(UserAccount, email=email)
            serializer = UpdateProfileSerializer(
                instance, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response("successfully updated your profile")
            
        return Response("Incomplete updation! Please try with valid data")
    
    def delete(self, request):
        payload = tokenValidation(request)
        email = payload.get("email")
        if email:
            instance = get_object_or_404(UserAccount, email=email)
            instance.delete()            
            return Response("Successful in deleting a profile.")
        
        return Response("Unsuccessful in deleting a profile.")
