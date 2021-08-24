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
        if id is not 0:
            user = User.objects.get(id_user=id)
            serializer = UserSerializer(user, many=False)
        else:
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
@api_view(['GET','POST','DELETE','PUT'])
def folderApi(request,id=0):
    if request.method == 'GET':
        if id is not 0:
            folder = Folder.objects.get(id_folder=id)
            serializer = FolderSerializer(folder, many=False)
        else:
            folders = Folder.objects.all()
            serializer = FolderSerializer(folders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        folder = Folder.objects.get(id_folder=id)
        serializer = FolderSerializer(folder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        folder = Folder.objects.get(id_folder=id)
        folder.delete()
        return JsonResponse("Deleted successfully", safe=False)
@api_view(['GET','POST','DELETE','PUT'])
def taskApi(request,id=0):
    if request.method == 'GET':
        if id is not 0:
            task = Task.objects.get(id_task=id)
            serializer = TaskSerializer(task, many=False)
        else:
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        task = Task.objects.get(id_task=id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task = Task.objects.get(id_task=id)
        task.delete()
        return JsonResponse("Deleted successfully", safe=False)
@api_view(['GET','POST','DELETE','PUT'])
def subtaskApi(request,id=0):
    if request.method == 'GET':
        if id is not 0:
            subtask = Sub_task.objects.get(id_sub_task=id)
            serializer = SubTaskSerializer(subtask, many=False)
        else:
            subtasks = Sub_task.objects.all()
            serializer = SubTaskSerializer(subtasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SubTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        subtask = Sub_task.objects.get(id_sub_task=id)
        serializer = SubTaskSerializer(subtask, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        subtask = Sub_task.objects.get(id_sub_task=id)
        subtask.delete()
        return JsonResponse("Deleted successfully", safe=False)
