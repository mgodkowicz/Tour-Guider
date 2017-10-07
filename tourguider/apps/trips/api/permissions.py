from rest_framework.permissions import IsAuthenticated, IsAdminUser


class IsAdminOrReadOnly(IsAdminUser):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return super(IsAdminOrReadOnly, self).has_permission(request, view)
