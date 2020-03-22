"""
Purpose: File holds all user related model declarations.

Date Created: 2/7/2020
"""
from datetime import datetime
from django.db import models
from django.conf import settings

from user.queries.usermanagers import UserManager

class UserDetail(models.Model):
    """
    Model holds all fields and business validation logic that corresponds with
    the Author model class.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, blank=True, null=True)
    occupation = models.CharField(max_length=30, default=None, blank=True, null=True)
    about_me_description = models.CharField(max_length=300, default=None, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True, default=datetime.now)
    date_created = models.DateTimeField(blank=True, null=True, default=datetime.now)

    objects = UserManager()

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.email
