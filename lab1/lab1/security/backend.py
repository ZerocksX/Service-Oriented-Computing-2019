from lab1.models.user import User


class MyBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            return User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
