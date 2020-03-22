"""
Purpose: File contains handlers for the JWT authentication process.

Date created: 2/25/2020
"""

from user.serializers.userserializer import UserSerializer

def my_jwt_response_handler(token, user=None, request=None):
    """Function returns a JWT payload reposnse."""
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }
    