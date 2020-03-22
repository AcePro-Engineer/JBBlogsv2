"""Script holds all url mappings for the user django app.
"""
from django.urls import path

from user.views.userviews import (
    CurrentUser,
    UserList
)

urlpatterns = [
    path('currentuser/', CurrentUser.as_view()),
    path('users/', UserList.as_view()),
]
