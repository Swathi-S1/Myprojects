from django.shortcuts import render
from apiregister.models import StudentClass
from django.contrib.auth.models import User

from apiregister.serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class TeacherRegisterView(APIView):
    print("jjjjjjjj")
    def get(self, request, format=None):
        user = User.objects.all()        
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)