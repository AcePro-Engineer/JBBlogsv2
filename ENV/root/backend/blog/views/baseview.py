"""
Purpose: Base class for all blog application views.
         all generic level logic will be placed in
         this view.

Date created: 2/5/2020
"""

# Handles printing the exception stack trace to console window.
import traceback

from django.http import JsonResponse
from rest_framework.views import APIView

class BaseAPIView(APIView):
    """Base class for all classed based views
       located in this django application.
    """

    def set_data_service_obj(self, data_service_obj):
         """Method initializes the data_service object.
         """
         
         self.data_service = data_service_obj

    def get_error_message(self, message, status_code):
        """Function returns a JSON reposne object that
           holds the generated error message and corresponding
           http error status code.
        """

        traceback.print_exc()
        return JsonResponse({'message': message}, status=status_code)
        