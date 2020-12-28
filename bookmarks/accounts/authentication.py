from django.contrib.auth.models import User



class EmailAuthBackend(object):
    """
    Authenticate using an email address.
    Django provides a simple way to define your own
    authentication backends. An authentication backend
    is a class that provides the following tow methods.
    """

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
