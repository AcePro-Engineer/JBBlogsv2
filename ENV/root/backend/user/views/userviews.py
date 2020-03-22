"""
Purpose: View(s) handle all user related request operations.

Date created: 2/24/2020
"""

from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_auth.registration.views import RegisterView

from  user.serializers.userserializer import (
    UserSerializer, 
    UserSerializerWithToken
)

from user.views.userbaseview import UserBaseAPIView
from services.utils.errors.exceptions import UserError

User = get_user_model()

class CurrentUser(UserBaseAPIView):
    """Class based view handles requests for
       existing users in the database.
    """
    def post(self, request):
        try:

            user_serializer = UserSerializer(request.user)
            return Response(user_serializer.data)

        except UserError as e:
            return self.get_error_message(e.detail, e.status_code)
        except Exception as e:
            traceback.print_exc()

class UserList(UserBaseAPIView):
    """Class based view handles user sign-up requests.
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        try:

            serializer = UserSerializerWithToken(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        except UserError as e:
            return self.get_error_message(e.detail, e.status_code)
        except Exception as e:
            traceback.print_exc()

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomRegisterView(RegisterView):
        queryset = User.objects.all()
