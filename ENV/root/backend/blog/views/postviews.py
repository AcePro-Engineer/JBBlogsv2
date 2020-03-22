"""
Purpose: Class handles all GET/PUT/POST/HEADER/PATCH requests
         for Post related information.

Date created: 2/1/2020
"""

# Handles printing the exception stack trace to console window.
import traceback
import json

from rest_framework import status

from rest_framework.parsers import (
    JSONParser, 
    MultiPartParser,
    FormParser
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from blog.views.baseview import BaseAPIView

from django.http import JsonResponse

from blog.serializers.blogpostserializers import BlogPostSerializer

from blog.serializers.blogserializers import (
    HeadingSerializer, 
    PostSerializer, 
    CommentSerializer
)

from services.utils.errors.exceptions import UserError
from services.blogservices.dataservices.postdataservice import PostDataService
from services.utils.customserilizers.heading_custom_serializer import HeadingCustomSerializer
from services.utils.customserilizers.post_custom_serilizer import PostCustomSerializer
from services.permissions.userpermissions import (
    IsBlackListedOrAllowed,
    IsLoggedInOrReadOnly
)

#region Post View
class PostView(IsLoggedInOrReadOnly, BaseAPIView):
    """Class handles all GET related client requests."""

    permission_classes = [AllowAny]

    def __init__(self):
        """Method handles all default initializations for the
           DraftView class.
        """

        self.set_data_service_obj(PostDataService())

    #region Operation Methods
    def get_post(self, slug):
        """Returns a blog Post that corresponds
           with the passed in slug value.
        """
        return self.data_service.get_post_by_slug(slug)
    #endregion

    #region Client Request Handling Methods
    def get(self, request, slug, format_spec=None):
        """Function handles all client GET requests."""
        serialized_post = None

        try:
            blog_post = self.get_post(slug)
            serialized_post = PostSerializer(blog_post)
        except UserError as e:
            return self.get_error_message(e.detail, e.status_code)
        except Exception as e:
            traceback.print_exc()

        return JsonResponse(serialized_post.data, safe=False)

    #endregion
#endregion

#region Draft View
class DraftView(BaseAPIView):
    """View is responsible for creating drafts."""
    
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, JSONParser, FormParser)
    authentication_classes  = (JSONWebTokenAuthentication,)

    def __init__(self):
        """Method handles all default initializations for the
           DraftView class.
        """

        self.set_data_service_obj(PostDataService())

    #region Operations Methods
    def save_draft(self, new_heading, new_post):
        """Creates and saves new blog Heading and Posts
           to the database.
        """
        self.data_service.save_as_draft(new_heading, new_post)
    #endregion

    #region Client Request Handling Methods
    def post(self, request):
        """Method handles all client POST requests for this view."""

        my_message = {
            'message': 'request failed'
        }

        try:

           headingcustomserializer = HeadingCustomSerializer(request.data)
           postcustomserializer = PostCustomSerializer(request.data)

           new_heading = headingcustomserializer.generate()
           new_post = postcustomserializer.generate(new_heading)

           my_message = {
            'message': 'request succeeded!'
           }
           
           if new_heading is not None and new_post is not None:
               self.save_draft(new_heading, new_post)
               return JsonResponse(my_message, status=status.HTTP_201_CREATED)

        except UserError as e:
            return self.get_error_message(e.detail, e.status_code)
        except Exception as e:
            traceback.print_exc()

        return JsonResponse(my_message, status=status.HTTP_400_BAD_REQUEST)
        #endregion
#endregion

#region Publish View
class PublishView(BaseAPIView):
    """View is reponsible for publishing posts."""

    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, JSONParser, FormParser)
    authentication_classes  = (JSONWebTokenAuthentication,)

    def __init__(self):
        """Method handles all default initializations for the
           PublishView class.
        """

        self.set_data_service_obj(PostDataService())

    #region Operation Methods
    def publish(self, new_heading, blog_post):
        """Method publishes blog posts."""

        self.data_service.publish(new_heading, blog_post)
    #endregion

    #region Client Request Hanlding Methods
    def post(self, response):
        """Method handles all client POST requests for this view."""

        blog_heading = None
        blog_post = None
        temp = None # Used to recieve Empty comment instance.

        try:

            serializer = PostSerializer(data=response.data)

            if serializer.is_valid():
                blog_heading, blog_post, temp = serializer.save()
                self.publish(blog_heading, blog_post)
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

        except UserError as e:
            return self.get_error_message(e.detail, e.status_code)
        except Exception as e:
            traceback.print_exc()
    #endregion
#endregion

#region Edit Post View
class EditPostView(BaseAPIView):
    """View is responsible for saving post changes to the database.."""

    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, JSONParser, FormParser)
    authentication_classes  = (JSONWebTokenAuthentication,)

    def __init__(self):
        """Method handles all default initializations for the
           EditPostView class.
        """

        self.set_data_service_obj(PostDataService())

    def save_changes(self, edited_post_data):
        """Method saves all changes to the corresponding
           post data.
        """
        self.data_service.edit(edited_post_data)

    def put(self, request):
        """Method handles all client PUT requests."""
        #REMEMBER: Put requests are idempotent only use
        #          when data MUST be updated. ie. update
        #          be retried after a request failure.
        pass

    def patch(self, request):
        """Method handles all client PATCH requests."""
        pass
#endregion

#region Comment View

"""
Not sure if I really need a Comment related view.
"""

#endregion
