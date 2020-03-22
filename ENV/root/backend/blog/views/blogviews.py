"""
Purpose: Class handles all GET/PUT/POST/HEADER/PATCH requests 
         for Heading related information.

Date Created: 1/21/2020
"""
# Handles printing the exception stack trace to console window.
import traceback

from rest_framework.permissions import AllowAny

from blog.views.baseview import BaseAPIView

from django.http import JsonResponse

from blog.serializers.blogserializers import HeadingSerializer
from services.blogservices.dataservices.headingdataservice import HeadingDataService

from services.utils.errors.exceptions import UserError

#region Blog Headings View
class HeadingsView(BaseAPIView):

    permission_classes = [AllowAny]

    def __init__(self):
        """Method handles all default initializations for the
           HeadingsView class.
        """

        self.set_data_service_obj(HeadingDataService())

    """Class handles all blog "headings" related client requests.
    """
    def get_blog_headings(self, num_of_days: int):
        return self.data_service.get_lastest_headings_by_num_of_days(num_of_days)

    def get(self, request, days: int, format_spec=None):
        """Function handles all client GET requests"""

        try:
            blog_headings = self.get_blog_headings(days)
            serialized_headings = HeadingSerializer(blog_headings, many=True)
        except UserError as e:
            return self.get_error_message(e.detail, e.status_code)
        except Exception as e:
            traceback.print_exc()
        
        return JsonResponse(serialized_headings.data, safe=False)
#endregion
