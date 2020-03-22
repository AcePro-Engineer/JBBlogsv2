"""
Purpose: This class is used to perform all data related
         operations for all heading model instances.

Date Created: 1/21/2020
"""
# For rendering the stack trace
import sys
import traceback

from django.db import IntegrityError, transaction

from rest_framework import status

from blog.models.blog import Heading 

from services.utils.errors.exceptions import (
        UserError,
        InvalidBlogHeadingValueError,
        InvalidBlogPostValueError,
        InvalidPostCommentValueError  
)

#region Heading data logic
class HeadingDataService():
    """Class holds all logic that handles all Heading
       related information processing operations.
    """

    #region Error Messages
    InvalidBlogHeadingTitle = "All headings must have a title."
    InvalidBlogHeadingDescription = "All headings must have a description."
    BlogHeadingLessThanFiveChars = "All headings must be atleast 5 characters."
    BlogHeadingGreaterThanOneHundredChars = "All headings must less than 100 characters."
    MisingBlogHeadingUser = "All headings must have a author."
    #endregion

    #region Data Retrieval

    def get_heading(self, heading_key:int) -> Heading:
        """Function returns a heading model instance.
        
        params: heading_key - heading model id.
        """
        
        if heading_key > 0:
            return Heading.blogheadings.single_blog_heading(heading_key)
        
        return None

    def get_lastest_headings_by_num_of_days(self, number_of_days: int):
        """Function returns a queryset of headings delimited by the number_of_days
        parameter.

        params: number_of_days - Number of days used to create the corresponding heading
                                    date range value.
        """

        try:

            if number_of_days > 0:
                return Heading.blogheadings.get_headings_by_number_of_days(number_of_days)
            else:
                raise InvalidNumberOfDaysError("Number of days must greater than 0", status_code=400)

        except UserError as e:
            traceback.print_exc()
            raise
        except Exception as e:
            traceback.print_exc()
            raise
        
        return None

    #endregion

    #region Data manipulation logic

    def create_heading(self, new_heading):
        """Method creates a new Heading object in the database."""

        # Developer Note: This method is never called on it's own(nor should it ever be called on it's own)
        #                 Hence it is already apart of a transaction block so there is no need to put 
        #                'with transaction...' logic here in this method.

        try:

            self.validate_model(new_heading)
            return Heading.blogheadings.create_heading(new_heading)

        except UserError as e:
            traceback.print_exc()
            raise
        except Exception as e:
            traceback.print_exc()
            raise

        return None

    def update_heading(self, heading_key, new_heading_data):
        """Method updates an existing Heading record."""
        try:

            with transaction.atomic():
                self.validate_model(new_heading_data)
                old_heading_data = get_heading(heading_key)
                Heading.blogheadings.edit_heading(old_heading_data, new_heading_data)

        except UserError as e:
            traceback.print_exc()
            raise
        except IntegrityError as e:
            traceback.print_exc()
            raise
        except Exception as e:
            traceback.print_exc()
            raise

    #endregion

    #region Heading Data validation logic

    def validate_model(self, heading):
        """Method holds all Heading related business validation logic.
        """
        if heading.heading_title is None:
            raise InvalidBlogHeadingValueError(detail=self.InvalidBlogHeadingTitle, status_code=status.HTTP_400_BAD_REQUEST)
        if heading.description is None:
            raise InvalidBlogHeadingValueError(detail=self.InvalidBlogHeadingDescription, status_code=status.HTTP_400_BAD_REQUEST)
        if len(heading.description) < 5:
            raise InvalidBlogHeadingValueError(detail=self.BlogHeadingLessThanFiveChars, status_code=status.HTTP_400_BAD_REQUEST)
        if len(heading.description) > 100:
            raise InvalidBlogHeadingValueError(detail=self.BlogHeadingGreaterThanOneHundredChars, status_code=status.HTTP_400_BAD_REQUEST)
        if heading.user is None:
            raise InvalidBlogHeadingValueError(detail=self.MisingBlogHeadingUser, status_code=status.HTTP_400_BAD_REQUEST)

    #endregion

#endregion