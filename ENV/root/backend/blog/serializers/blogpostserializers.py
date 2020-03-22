"""
Purpose: Class(es) hold serialization logic for multiple objects
         nested in the same response object.

Date created: 2/7/2020
"""

# Handles printing the exception stack trace to console window.
import sys
import traceback

from rest_framework import serializers

from blog.models.blog import (
    Heading, 
    Post, 
    Comment
)

from .blogserializers import (
    HeadingSerializer,
    PostSerializer,
    CommentSerializer
)

#region Blog Post Serializer logic
class BlogPostSerializer(serializers.ModelSerializer):
    heading = HeadingSerializer(required=False)
    post = PostSerializer(required=False)
    comment = CommentSerializer(required=False)

    def get_heading_model(self, data):
        """Returns a heading model instance."""
        blog_heading = Heading (
            title=data.get('title', data),
            description=data.get('description', data),
            preview_image=data.get('preview_image', data),
            date_modified=data.get('date_modified', data),
            date_created=data.get('date_created', data),
            author=data.get('author', data)
        )

        return blog_heading

    def get_post_model(self, data):
        """Returns a post model instance."""
        blog_post = Post(
            title=data.get('title', data),
            article=data.get('article', data),
            heading=data.get('heading', data),
            slug=data.get('slug', data),
            date_modified=data.get('date_modified', data),
            date_created=data.get('date_created', data),
            status=data.get('status', data),
            image_URL=data.get('status', data),
            author=data.get('author', data)
        )

        return blog_post

    def get_comment_model(self, data):
        """Returns a comment model instance."""
        post_comment = Comment(
            comment_paragraph=data.get('comment_paragraph', data),
            date_modified=data.get('date_modified', data),
            date_created=data.get('date_created', data)
        )

        return post_comment

    def deserialize(self, data):
        """Returns all deserialized data's correspoding model instances."""

        blog_heading = None
        blog_post = None
        blog_comment = None

        number_of_created_instances = 0

        heading_data = data.pop('heading')
        post_data = data.pop('post')
        comment_data = data.pop('comment')

        if heading_data is not None:
            blog_heading = self.get_heading_model(heading_data)

        if post_data is not None:
            blog_post = self.get_post_model(post_data)

        if comment_data is not None:
            blog_comment = self.get_comment_model(comment_data)
            
        return blog_heading, blog_post, blog_comment

    def create(self, validated_data):
        """Overriding the default rest serializer create
           function with logic that is specific for my
           project requirements.
        """
        try:
            return self.deserialize(validated_data)
        except Exception as e:
            traceback.print_tb(sys.exc_info[2])
            raise

    def update(self, validated_data):
        """Overriding the default rest serializer create
           function with logic that is specific for my
           project requirements.
        """
        try:
            return self.deserialize(validated_data)
        except Exception as e:
            traceback.print_tb(sys.exc_info[2])
            raise

#endregion