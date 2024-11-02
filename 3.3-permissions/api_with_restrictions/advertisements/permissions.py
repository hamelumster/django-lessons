from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """Права доступа для редактирования и удаления объявления."""
    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return obj.creator == request.user
        return True