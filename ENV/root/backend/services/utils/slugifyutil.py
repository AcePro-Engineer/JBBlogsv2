"""
Purpose: Script slugifies Heading title values.

Date created: 2/19/2020
"""
from django.utils.text import slugify

def generate_slug(title, new_slug=None):
    """Creates a new slug value based on the passed
       title value.
    """
    slug = None
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(title)

    return slug
