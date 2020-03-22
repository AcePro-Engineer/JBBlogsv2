"""
Purpose: Performs custom serilization of all heading related data.
"""

from blog.models.blog import Heading

from django.contrib.auth.models import User

class HeadingCustomSerializer():
    """Class generates a Heading model instance via 
       raw response object data.
    """

    def __init__(self, data):
        self.data = data

    def generate(self):
        """Returns a Post model instance."""

        username = self.data['user']
        user = User.objects.get(username=username)
        
        blog_heading = Heading(
            heading_title=self.data['heading_title'],
            description=self.data['description'],
            preview_image=self.data['preview_image'],
            user=user
        )

        return blog_heading
