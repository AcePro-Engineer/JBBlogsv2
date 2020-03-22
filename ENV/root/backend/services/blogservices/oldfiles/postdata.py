"""
Purpose: This script is used to perform all data related
         operations for all blog post model objects.

Date created: 2/5/2020
"""

"""
# Used to print the exception stack trace to console window.
import sys
import traceback

from rest_framework import status

from blog.models.blog import (
    Post,
    Comment
)

from .blogdata import create_heading

from services.utils.errors.exceptions import (
    UserError,
    InvalidValueError
)

#region Post data logic

#### Post Data Retrieval ####
def get_post_by_slug(slug):
    """ Retrieves the corrsponding Post information by
        the slug value.
    """
    try:
        if slug is not None:
            return Post.blogposts.get_post_by_slug(slug)
        else:
            raise InvalidValueError("Please provide a valid slug value.", status_code=status.HTTP_400_BAD_REQUEST)
    
    except UserError as e:
        traceback.print_exc()
        raise
    except Exception as e:
        traceback.print_exc()
        raise 

    return None

##### Post Data Manipulation #####

def save_as_draft(new_heading, new_post):
    """Function creates and/or publishes the blog heading 
       and it's corresponding blog post information.
    """
    
    try:
        create_heading(new_heading)
        new_post.validate_model()

        Post.blogposts.save_post_as_draft(new_post)

    except UserError as e:
        traceback.print_exc()
        raise
    except Exception as e:
        traceback.print_exc()
        raise

def publish(new_heading, blog_post):
    """Method publishes the corresponding blog Post."""

    try:

        if new_heading is not None:
            create_heading(new_heading)

        blog_post.validate_model()
        Post.blogposts.publish_post(blog_post.slug, new_post)

    except UserError as e:
        traceback.print_exc()
        raise
    except Exception as e:
        traceback.print_exc()
        raise

def edit(new_post_data):
    """ Updates existing blog Post record with
        new blog Post data recieved from the client.
    """
    try:

        new_post_data.validate_model()
        old_post_data = get_post_by_slug(new_post_data.slug)

        Post.blogposts.edit_post(old_post_data, new_post_data)
    
    except UserError as e:
        traceback.print_exc()
        raise
    except Exception as e:
        traceback.print_exc()
        raise

#endregion

#region Comment data logic

#endregion
"""