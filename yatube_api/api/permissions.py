from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    '''Проверяем, что метод безопасен(GET и проч.)
       и текущий пользователь - это его автор.'''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
