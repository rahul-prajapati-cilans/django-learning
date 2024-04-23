from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.models import Profile, User
from app.serializers import ProfileSerializer, UserSerializer

# Create your views here.


class UserList(APIView):
    def get(self, request):
        user_data = Profile.objects.all()
        serializer = ProfileSerializer(user_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserDetail(APIView):
    def get(self, request, pk):
        user_data = User.objects.get(pk=pk)
        serializer = UserSerializer(user_data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user_data = User.objects.get(pk=pk)
        serializer = UserSerializer(user_data, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        user_data = User.objects.get(pk=pk)
        serializer = UserSerializer(user_data, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user_data = User.objects.get(pk=pk)
        user_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
