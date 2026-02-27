from rest_framework.permissions import BasePermission

class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return request.user.role=="doctor" and request.user.is_authenticated

class IsPatient(BasePermission):
    def has_permissions(self,request,view):
        return request.user.role=="patient" and request.user.is_authenticated