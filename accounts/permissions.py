from rest_framework.permissions import BasePermission

class SellerPermissions(BasePermission):

    message = "not access"

    def has_permission(self, request, view):
        return request.user.is_authenticated and hasattr(request.user, 'seller')


    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True

