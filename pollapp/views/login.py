from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import generics, exceptions
from rest_framework.response import Response

from pollapp.authentication import generate_access_token


@api_view(['POST'])
def login(request):
    login = request.data.get('login')
    password = request.data.get('password')
    user = User.objects.filter(username=login).first()

    if User is None:
        raise exceptions.AuthenticationFailed('User not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect password')

    response = Response()
    token = generate_access_token(user)
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }

    return response

@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie(key='jwt')
    response.data = {
        'message': 'Success'
    }

    return response