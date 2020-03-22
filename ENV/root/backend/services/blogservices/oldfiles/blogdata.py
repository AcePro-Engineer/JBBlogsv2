"""
Purpose: This script is used to perform all data related
         operations for all blog heading model objects.

Date Created: 1/21/2020
"""

"""
# For rendering the stack trace
import sys
import traceback

from blog.models.blog import Heading 

from services.utils.errors.exceptions import UserError

#region Heading data logic

##### Data Retrieval #####

def get_heading(heading_key:int) -> Heading:
    """Function returns a heading model instance.
       
       params: heading_key - heading model id.
    """
    
    if heading_key > 0:
        return Heading.blogheadings.single_blog_heading(heading_key)
    
    return None

def get_lastest_headings_by_num_of_days(number_of_days: int):
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

##### Data manipulation logic #####

def create_heading(new_heading):
    """Method creates a new Heading object in the database."""

    try:

        new_heading.validate_model()
        Heading.blogheadings.create_heading(new_heading)

    except UserError as e:
        traceback.print_exc()
        raise
    except Exception as e:
        traceback.print_exc()
        raise

def update_heading(heading_key, new_heading_data):
    """Method updates an existing Heading record."""
    try:

        new_heading_data.validate_model()
        old_heading_data = get_heading(heading_key)
        Heading.blogheadings.edit_heading(old_heading_data, new_heading_data)

    except UserError as e:
        traceback.print_exc()
        raise
    except Exception as e:
        traceback.print_exc()
        raise
#endregion
"""
