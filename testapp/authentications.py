from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get('username')
        if username is None:
            return None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('No Such type of user')
        return (user, None)


class CustomAuthentication_case_2(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get('username')
        key = request.GET.get('key')
        print("==========================")
        print(username)
        print(key)
        if username is None or key is None or username == '' or key == '':
            return None
        print("how")
        case_1 = len(key) == 7
        case_2 = key[0] == username[-1].lower()
        case_3 = key[2] == 'Z'
        case_4 = key[4] == username[0]

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed(
                'Your provided username is invalid,plz provide valid username to access endpoint.')
        if case_1 and case_2 and case_3 and case_4:
            return (user, None)
        raise AuthenticationFailed(
            'Your provided key is invalid,plz provide valid key to access endpoint.')
