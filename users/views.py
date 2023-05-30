from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from users.models import User

from brine.constants import EMAIL, ERROR, FIRST_NAME, LAST_NAME, MESSAGE, PASSWORD, USERNAME

# Create your views here.
class UserCreate(APIView):
    def post(self, request):
        """ create user"""
        
        try:
            payload = request.data
            first_name = payload.get(FIRST_NAME)
            last_name = payload.get(LAST_NAME)
            email = payload.get(EMAIL)
            username = payload.get(USERNAME)
            password = payload.get(PASSWORD)
            if not username:
                return Response({ MESSAGE: ERROR }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            else:
                User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password )
                data = { MESSAGE: "User Created Successfully" }
                return Response(data, status=status.HTTP_201_CREATED)        
        except Exception as e:
            print(e)
            return Response({ MESSAGE: ERROR }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
