"""
Purpose: File holds all custom django permissions logic.

Date created: 2/26/2020
"""

from rest_framework import permissions

class IsBlackListedOrAllowed(permissions.BasePermission):
    #Gobal permission check for blacklisted IPs.

    def has_permission(self, request, view):
        addr = request.META['REMOTE_ADDR']
        is_blacklisted = Blacklist.objects.filter(ip_addr=addr).exists()
        return is_blacklisted

class IsLoggedInOrReadOnly(permissions.BasePermission):
    """
    Method checks user permissions.
    """
    #Note all read only requests are valid in this application.
    #Unless read only action refers to sensitive data.

    def has_object_permission(self, request, view, obj):
        """
        Function checks all object permissions.
        """

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.owner == request.user
