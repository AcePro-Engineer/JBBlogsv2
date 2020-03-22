"""
Purpose: Holds all logic and model validation associated with
         blog related models.
"""

from django.db import models
from datetime import datetime
from django.conf import settings

from blog.queries.blogmanagers import (
    HeadingManager, 
    HeadingQuerySet, 
    PostManager, 
    PostQuerySet
)

#region STATUS Tuple
# Tuple holds the Post status values.
# These values will be used to control
# Post Creation in the BLOG application.
STATUS = (
    [0, "Draft"], 
    [1, "Publish"]
)
#endregion

#region Blog Heading Model

class Heading(models.Model):
    """
    Model holds all fields and methods that pretain to the blog_blog_heading table.
    """
    
    #All table fields
    heading_title = models.CharField(max_length=100, default=None, blank=True, null=True)
    description = models.CharField(max_length=300, default=None, blank=True, null=True)
    preview_image = models.ImageField(upload_to='media/images', default=None, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True, default=datetime.now)
    date_created = models.DateTimeField(blank=True, null=True, default=datetime.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, blank=True, null=True)

    # Custom model manager(s)
    blogheadings = HeadingManager.from_queryset(HeadingQuerySet)()

    class Meta:
        ordering = ['-date_created']

#endregion

#region Blog Post Model

class Post(models.Model):
    """
    Model holds all fields and methods that pretain to the blog_blog_post table. 
    """
    
    #All table fields
    post_title = models.CharField(max_length=100, default=None, blank=True, null=True)
    article = models.TextField(default=None, blank=True, null=True)
    heading = models.ForeignKey(Heading, on_delete=models.CASCADE, default=None, blank=True, null=True)
    slug = models.SlugField(max_length=500, unique=True, default=None, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True, default=datetime.now)
    date_created = models.DateTimeField(blank=True, null=True, default=datetime.now)
    status = models.IntegerField(choices=STATUS, default=0)
    post_image = models.ImageField(upload_to='media/images', default=None, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, blank=True, null=True)

    # Custom model manager(s)
    blogposts = PostManager.from_queryset(PostQuerySet)()

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title
        
#endregion

#region Blog Comment Model
class Comment(models.Model):
    """
    Model holds all fields and methods that pretain to the blog_blog_comment table. 
    """

    #All table fields
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None, blank=True, null=True)
    comment_paragraph = models.CharField(max_length=2000, default=None, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True, default=datetime.now)
    date_created = models.DateTimeField(blank=True, null=True, default=datetime.now)

    class Meta:
        ordering = ['-date_created']

#endregion
