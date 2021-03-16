from account.models import User


class PhoneAuthBackend(object):
    """
    Authenticate using email and phone.
    """

    def authenticate(self, request, email=None, password=None, phone_number=None):
        try:
            user = User.objects.filter(email=email, phone_number=phone_number)
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
