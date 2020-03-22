"""
Purpose: Class holds all serialization logic for the corresponding
         blog model classes.


Date Created: 1/21/2020
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

#region Heading Serializer
class HeadingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Heading
        fields = '__all__'

    def get_custom_model(self, data):
        """Returns an instance of the Heading class."""
        blog_heading = Heading (
            heading_title=data.get('heading_title', data),
            description=data.get('description', data),
            preview_image=data.get('preview_image', data),
            user=data.get('user', data)
        )

        return blog_heading

    def create(self, validated_data):
        """Overriding the default rest serializer create
           function with logic that is specific for my
           project requirements.
        """
        try:
            return self.get_custom_model(validated_data)
        except Exception as e:
            traceback.print_tb(sys.exc_info[2])
            raise

    def update(self, validated_data):
        """Overriding the default rest serializer update
           function with logic that is specific for my
           project requirements.
        """
        try:
            return self.get_custom_model(validated_data)
        except Exception as e:
            traceback.print_tb(sys.exc_info[2])
            raise
#endregion

#region Post Serializer
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

    def get_custom_model(self, data):
        """Returns an instance of the Post class."""
        blog_post = Post(
            post_title=data.get('post_title', data),
            article=data.get('article', data),
            slug=data.get('slug', data),
            status=data.get('status', data),
            user=data.get('user', data)
        )

        return blog_post

    def create(self, validated_data):
        """Overriding the default rest serializer create
           function with logic that is specific for my
           project requirements.
        """
        try:
            return self.get_custom_model(validated_data)
        except Exception as e:
            traceback.print_tb(sys.exc_info[2])
            raise

    def update(self, validated_data):
        """Overriding the default rest serializer update
           function with logic that is specific for my
           project requirements.
        """
        try:
            return self.get_custom_model(validated_data)
        except Exception as e:
            traceback.print_tb(sys.exc_info[2])
            raise
#endregion

#region Comment Serializer
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

    def get_custom_model(self, data):
        """Returns an instance of the Post class."""
        post_comment = Comment(
            post=data.get('post', data),
            comment_paragraph=data.get('comment_paragraph', data),
        )

        return post_comment

    def create(self, validated_data):
        """Overriding the default rest serializer create
           function with logic that is specific for my
           project requirements.
        """
        try:
            return self.get_custom_model(validated_data)
        except Exception as e:
            traceback.print_tb(sys.exc_info[2])
            raise

    def update(self, validated_data):
        """Overriding the default rest serializer update
           function with logic that is specific for my
           project requirements.
        """
        try:
            return self.get_custom_model(validated_data)
        except Exception as e:
            traceback.print_tb(sys.exc_info[2])
            raise       
#endregion
