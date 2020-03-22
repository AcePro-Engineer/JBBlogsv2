"""
Purpose: All class(es) in this file hold all querying operations for 
         all blog post related models (heading, post, comment)

Date Created: 1/21/2020
"""
# For rendering the stack trace
import sys
import traceback

# datetime and timedelta are used in date range calculations.
from datetime import (
    datetime, 
    timedelta
)

from django.db.models import (
    Manager, 
    QuerySet
)

#region Heading Manager/QuerySet
class HeadingQuerySet(QuerySet):
    """
    Custom queryset class for the HeadingManager model manager class.
    """
    #region Data retrieval methods
    def single_blog_heading(self, pkey: int):
        """Function returns a single heading model object.

           params: pkey - Id of the corresponding heading object.
        """
        return self.get(id=pkey)

    def get_blog_headings(self, limit:int):
        """Returns a number of heading objects limited
           by the passed in limit parameter value.

           params: limit - number of objects that the client
                           wishes to fetch from the database.
        """
        return self.all()[:limit]

    def get_headings_by_datecreated_range(self, from_date, to_date):
        """Function returns a queryset of heading objects that fall in
           the specified "date created" date range.

           params: from_date - Starting created date for the specified date range.
                   to_date   - Ending created date for the specified date range.
        """
        return self.filter(date_created__gte=from_date, date_created__lte=to_date)
    
    def get_headings_by_datemodified_range(self, from_date, to_date):
        """ Function returns a queryset of heading objects that fall in
            the specified "date modified" date range.

            params: from_date - Starting modified date for the specified date range.
                    to_date   - Ending modified date for the specified date range.
        """
        return self.filter(date_modified__gte=from_date, date_modified__lte=to_date)

    def get_headings_by_number_of_days(self, number_of_days):
        """Function returns a queryset of heading objects where the
           headings have been created within a certain time frame
           specified by the client. 
           
           ie. (today - the number of days) the client specifies in their request.

           params: number_of_days - Number of days that is subtracted from today's date.
        """
        from_date = datetime.today() - timedelta(days=number_of_days)
        return self.filter(date_created__gte=from_date, date_created__lte=datetime.today())
    #endregion

    #region Data Manipulation methods
    def create_heading(self, new_heading):
        """Method creates a new blog heading."""

        blog_heading = self.create(
            heading_title=new_heading.heading_title,
            description=new_heading.description,
            preview_image=new_heading.preview_image,
            user=new_heading.user
        )

        return blog_heading

    def edit_heading(self, old_heading_data, new_heading_data):
        """Updates the corresonding Heading record in the database."""

        old_heading_data.heading_title = new_heading_data.heading_title
        old_heading_data.description = new_heading_data.description
        old_heading_data.preview_image = new_heading_data.preview_image
        old_heading_data.date_modified = datetime.now()
        old_heading_data.user = new_heading_data.user

        old_heading_data.save()

    #endregion

class HeadingManager(Manager):
    """
    Model manager for the heading model class. 
    """

    def get_queryset(self):
        """
        Returns the custom queryset object associated with this 
        custom model manager.
        """
        try:
            return HeadingQuerySet(self.model, using=self._db)
        except Exception as e:
            traceback.print_tb(sys.exc_info()[2])
            raise
#endregion

#region Post Manager/QuerySet
class PostQuerySet(QuerySet):
    """Custom QuerySet class for the Post model manager.
    """
    #region Data retrieval
    def get_post_by_slug(self, slugdesc: str):
        """Returns a Post object by the specified SLUG value.
        """
        return self.get(slug=slugdesc)
    #endregion

    #region Data manipulation
    def save_post_as_draft(self, new_post):
        """Saves the blog post and corresponding heading to the
           database as a "draft".
        """
        blog_post = self.create(
            post_title=new_post.post_title,
            article=new_post.article,
            heading=new_post.heading,
            slug=new_post.slug,
            post_image=new_post.post_image,
            status=0,
            user=new_post.user
        )

        return blog_post

    def publish_post(self, post_slug, new_post):
        """ 'Publishes'(Creates/Updates) blog post and heading information.
        """
        blog_post = None

        if post_slug:
            blog_post = self.get_post_by_slug(post_slug)
            blog_post.status = 1
            blog_post.save()
        else:
            blog_post = self.create(
                post_title=new_post.post_title,
                article=nw_post.article,
                heading=blog_heading.id,
                slug=new_post.slug,
                post_image=new_post.post_image,
                status=1,
                user=new_post.user
            )

        return blog_post

    def edit_post(self, old_post_data, new_post_data):
        """updates the corresponding blog post and heading information.
        """
        
        old_post_data.post_title = new_post_data.post_title
        old_post_data.article = new_post_data.article
        old_post_data.heading = new_post_data.heading
        old_post_data.slug = new_post_data.slug
        old_post_data.date_modified = datetime.now()
        old_post_data.post_image = new_post_data.post_image
        old_post_data.status = new_post_data.status
        old_post_data.user = new_post_data.user

        old_post_data.save()

        return old_post_data

    def remove_post(self, post_slug):
        """Deletes the corresponding Post information from the database
           permently.
        """
        pass

    def disable_post(self, post_slug):
        """Marks the corresponding post as deleted in the database.
        """
        pass
    #endregion

class PostManager(Manager):
    """ Model manager for the Post model class.
    """
    def get_queryset(self):
        """Returns the custom queryset object associated with this 
           custom model manager.
        """
        try:
            return PostQuerySet(self.model, using=self._db)
        except Exception as e:
            traceback.print_tb(sys.exc_info[2])
            raise
#endregion
