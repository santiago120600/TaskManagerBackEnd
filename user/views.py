from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.models import User, Folder, Task, Sub_task
from user.serializers import UserSerializer, FolderSerializer, TaskSerializer, SubTaskSerializer

@api_view(['GET','POST','DELETE','PUT'])
def userApi(request,id=0):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        user = User.objects.get(id_user=id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user = User.objects.get(id_user=id)
        user.delete()
        return JsonResponse("Deleted successfully", safe=False)