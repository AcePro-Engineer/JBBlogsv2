"""
Purpose: All class(es) in this file hold all querying operations for
         the user model.

Date Created: 1/21/2020
"""

# For rendering the stack trace
import sys
import traceback

from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    """Model manager for the user model."""
    
    use_in_migrations = True

    def create_user(self, new_user):
        """Creates a new user instance and saves
           the new instance to the database.
        """
        user = self.model(
            username=new_user.username,
            first_name=new_user.first_name,
            last_name=new_user.last_name,
            occupation=new_user.occupation,
            about_me_description=new_user.about_me_description,
            email=new_user.email
        )

        user.set_password(new_user.password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """Creates a new 'super' user instance in the database."""
        print("I MADE IT")
        user = self.create_user(
            username=username,
            password=password
        )

        user.is_admin = True
        user.save(using=self._db)
        return user
