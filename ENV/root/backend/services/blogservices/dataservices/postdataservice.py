"""
Purpose: This class is used to perform all data related
         operations for all blog post model objects.

Date created: 2/5/2020
"""

# Used to print the exception stack trace to console window.
import sys
import traceback

from django.db import IntegrityError, transaction

from services.utils.slugifyutil import generate_slug

from rest_framework import status

from blog.models.blog import (
    Post,
    Comment
)

from .headingdataservice import HeadingDataService

from services.utils.errors.exceptions import (
    UserError,
    InvalidBlogHeadingValueError,
    InvalidBlogPostValueError,
    InvalidPostCommentValueError,
    InvalidValueError
)

#region Post data logic
class PostDataService():
     """Class holds all logic that handles all Post
        related information processing operations.
     """

     def __init__(self):
         """Method handles all default initializations for the
            PostDataService class.
         """
         self.heading_data_service = HeadingDataService()

     #region Error Messages
     InvalidBlogPostTitle = "All posts must have a title."
     BlogPostTitleLessThanFiveChars = "All blog post titles must be atleast 5 characters."
     BlogPostTitleGreaterThanOneHundredChars = "All blog post titles must less than 100 characters."
     InvalidBlogPostArticle = "All posts must have a article."
     BlogPostArticleMustBeTwoHundredChars = "All articles must be atleast 200 characters."
     InvalidBlogPostSlug = "All posts must have a slug."
     InvalidBlogPostStatus = "All posts must have a status."
     MissingBlogPostHeading = "All posts must have a heading."
     MissingBlogPostUser = "All posts must have a user."
     #endregion

     #region Post Data Retrieval

     def get_post_by_slug(self, slug):
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

     #endregion

     #region Post Data Manipulation

     def save_as_draft(self, new_heading, new_post):
         """Function creates and/or publishes the blog heading 
            and it's corresponding blog post information.
         """
        
         try:
             with transaction.atomic():
                created_heading = self.heading_data_service.create_heading(new_heading)
                new_post.heading = created_heading
                new_post.slug = generate_slug(created_heading.heading_title)
                self.validate_model(new_post)

                Post.blogposts.save_post_as_draft(new_post)

         except UserError as e:
             traceback.print_exc()
             raise
         except IntegrityError as e:
             traceback.print_exc()
             raise
         except Exception as e:
             traceback.print_exc()
             raise

     def publish(self, new_heading, blog_post):
         """Method publishes the corresponding blog Post."""

         try:

             with transaction.atomic():
                if new_heading is not None:
                    created_heading = self.heading_data_service.create_heading(new_heading)
                    blog_post.heading = created_heading
                    blog_post.slug = generate_slug(created_heading.heading_title)

                self.validate_model(blog_post)
                Post.blogposts.publish_post(blog_post.slug, new_post)

         except UserError as e:
             traceback.print_exc()
             raise
         except IntegrityError as e:
             traceback.print_exc()
             raise
         except Exception as e:
             traceback.print_exc()
             raise

     def edit(self, new_post_data):
         """ Updates existing blog Post record with
             new blog Post data recieved from the client.
         """
         try:

             with transaction.atomic():
                self.validate_model(new_post_data)
                old_post_data = get_post_by_slug(new_post_data.slug)

                Post.blogposts.edit_post(old_post_data, new_post_data)
        
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

     #region Post Data Validation

     def validate_model(self, post):
         """Method holds all Post related business validation logic.
         """
         if post.post_title is None:
             raise InvalidBlogPostValueError(detail=self.InvalidBlogPostTitle, status_code=status.HTTP_400_BAD_REQUEST)
         if len(post.post_title) < 5:
             raise InvalidBlogPostValueError(detail=self.BlogPostTitleLessThanFiveChars, status_code=status.HTTP_400_BAD_REQUEST)
         if len(post.post_title) > 100:
             raise InvalidBlogPostValueError(detail=self.BlogPostTitleGreaterThanOneHundredChars, status_code=status.HTTP_400_BAD_REQUEST)
         if post.article is None:
             raise InvalidBlogPostValueError(detail=self.InvalidBlogPostArticle, status_code=status.HTTP_400_BAD_REQUEST)
         if len(post.article) < 200:
             raise InvalidBlogPostValueError(detail=self.BlogPostArticleMustBeTwoHundredChars, status_code=status.HTTP_400_BAD_REQUEST)
         if post.slug is None:
             raise InvalidBlogPostValueError(detail=self.InvalidBlogPostSlug, status_code=status.HTTP_400_BAD_REQUEST)
         if post.status is None:
             raise InvalidBlogPostValueError(detail=self.InvalidBlogPostStatus, status_code=status.HTTP_400_BAD_REQUEST)
         if post.heading is None:
             raise InvalidBlogPostValueError(detail=self.MissingBlogPostHeading, status_code=status.HTTP_400_BAD_REQUEST)
         if post.user is None:
             raise InvalidBlogPostValueError(detail=self.MissingBlogPostUser, status_code=status.HTTP_400_BAD_REQUEST)

     #endregion

#endregion