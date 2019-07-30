# partesanato/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def root(request, format=None):
    return Response({
        'docs': reverse('docs', request=request, format=format),
        'account_login': reverse('account_login', request=request, format=format),
        'account_logout': reverse('account_logout', request=request, format=format),
        'account_signup': reverse('account_signup', request=request, format=format),
        'account_email': reverse('account_email', request=request, format=format),
        'account_password': reverse('account_set_password', request=request, format=format),
        'reset_password': reverse('account_reset_password', request=request, format=format),
        'rest_login': reverse('rest_login', request=request, format=format),
        'rest_logout': reverse('rest_logout', request=request, format=format),
        'rest_password_change': reverse('rest_password_change', request=request, format=format),
        'rest_user_details': reverse('rest_user_details', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format),
    })
