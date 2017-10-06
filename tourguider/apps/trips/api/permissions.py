from rest_framework.permissions import IsAuthenticated, IsAdminUser


class IsAuthenticatedNotPost(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.method != 'GET' and not request.user.is_superuser:
            request.data['private'] = True
        print(request.data)

        return super(IsAuthenticatedNotPost, self).has_permission(request, view)
