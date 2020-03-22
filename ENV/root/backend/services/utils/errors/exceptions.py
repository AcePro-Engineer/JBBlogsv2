"""All custom exception class for the "blog" application.

   Date created: 2/3/2020
"""
from rest_framework.exceptions import APIException
from rest_framework import status

#region UserError base class
class UserError(APIException):
   """Base for all custom exception classes."""
   status_code = status.HTTP_400_BAD_REQUEST
   default_detail = ""
   default_code = 'invalid'

   def __init__(self, detail, status_code=None):
      self.detail = detail

      if status_code is not None:
         self.status_code = status_code

#endregion

#region InvalidValue Error
class InvalidValueError(UserError):
   """Exception is used to handle invalid data values
      passed from the client.
   """
   pass
#endregion

#region InvalidNumberOfDays Error
class InvalidNumberOfDaysError(UserError):
    """Custom exception is raised when the client passes an
       invalid number of days value for the get_lastest_headings_by_num_of_days
       service application function.
    """
    pass
#endregion

#region InvalidBlogHeadingValue Error
class InvalidBlogHeadingValueError(UserError):
   """Custom exception is raised whenever a Heading model fails business code validation"""
   pass
#endregion

#region InvalidBlogPostValue Error
class InvalidBlogPostValueError(UserError):
   """Custom exception is raised whenever a Post model fails business code validation"""
   pass
#endregion

#region InvalidPostCommentValue Error
class InvalidPostCommentValueError(UserError):
   """Custom exception is raised whenever a Comment model fails business code validation"""
   pass
#endregion
