"""
Purpose: Performs custom serilization of all post related data.
"""

from blog.models.blog import Post

from django.contrib.auth.models import User

class PostCustomSerializer():
    """Class generates a Post model instance via 
       raw response object data.
    """

    def __init__(self, data):
        self.data = data

    def generate(self, blog_heading):
        """Returns a Post model instance."""

        username = self.data['user']
        user = User.objects.get(username=username)
        
        blog_post = Post(
            post_title=self.data['post_title'],
            article=self.data['article'],
            heading=blog_heading,
            slug=self.data['slug'],
            status=self.data['status'],
            post_image=self.data['preview_image'],
            user=user
        )

        return blog_post
