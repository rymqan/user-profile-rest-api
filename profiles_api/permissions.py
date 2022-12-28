from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit own profile"""
    
    def has_object_permission(self, request, view, obj):
        """Check user editing own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
    
    
class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to edit own status"""
    
    def has_object_permission(self, request, view, obj):
        """Check user editing own status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id