from django.shortcuts import render
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from django.contrib.auth.models import User  
from user.models import Folder, Task, Sub_task
from user.serializers import UserSerializer, FolderSerializer, TaskSerializer, SubTaskSerializer

from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.permissions import IsAuthenticated, AllowAny

@api_view(['GET','POST','DELETE','PUT'])
@permission_classes([IsAuthenticated])
def userApi(request,id=None):
    response = {}
    data = {}
    if id:
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            response['status'] = status.HTTP_404_NOT_FOUND
            response['message'] = 'No encontrado'
            response['data'] = []
            return Response(response)
    if request.method == 'GET':
        if id:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user, many=False)
            response['status'] = status.HTTP_200_OK
            response['message'] = 'OK'
            response['data'] = serializer.data
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            response['status'] = status.HTTP_200_OK
            response['message'] = 'OK'
            response['data'] = serializer.data
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            response['status'] =status.HTTP_201_CREATED
            response['message'] = 'Usuario creado'
            data['email'] = account.email
            data['username'] = account.username
            data['token'] = Token.objects.get(user=account).key
            response['data'] = data
            response['validations'] = []
        else:
            response['status'] =status.HTTP_400_BAD_REQUEST
            response['data'] = []
            response['message'] = 'Error de validaciones'
            response['validations'] =serializer.errors 
    elif request.method == 'PUT':
        if id:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                response['status'] =status.HTTP_202_ACCEPTED
                response['message'] = 'Usuario actualizado'
                response['validations'] = []
                response['data'] =serializer.data
            else:
                response['status'] =status.HTTP_400_BAD_REQUEST
                response['message'] = 'Error en validaciones'
                response['validations'] = serializer.errors
                response['data'] =[]
        else:
            response['status'] =status.HTTP_400_BAD_REQUEST
            response['message'] = 'Id no enviado'
            response['validations'] = []
            response['data'] = []
    elif request.method == 'DELETE':
        if id:
            user = User.objects.get(id=id)
            user.delete()
            response['status'] =status.HTTP_200_OK
            response['message'] = 'Eliminado correctamente'
            response['validations'] = []
            response['data'] =[]
        else:
            response['status'] =status.HTTP_400_BAD_REQUEST
            response['message'] = 'Id no enviado'
            response['validations'] = []
            response['data'] = []
    return Response(response)
@api_view(['GET','POST','DELETE','PUT'])
def folderApi(request,id=None):
    response = {}
    data = {}
    if id:
        try:
            folder = Folder.objects.get(id_folder=id)
        except ObjectDoesNotExist:
            response['status'] = status.HTTP_404_NOT_FOUND
            response['message'] = 'No encontrado'
            response['data'] = []
            return Response(response)
    if request.method == 'GET':
        if id:
            folder = Folder.objects.get(id_folder=id)
            serializer = FolderSerializer(folder, many=False)
            response['status'] = status.HTTP_200_OK
            response['message'] = 'OK'
            response['data'] = serializer.data
        else:
            folders = Folder.objects.all()
            serializer = FolderSerializer(folders, many=True)
            response['status'] = status.HTTP_200_OK
            response['message'] = 'OK'
            response['data'] = serializer.data
    elif request.method == 'POST':
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response['status'] = status.HTTP_201_CREATED
            response['message'] = 'Folder creado correctamente'
            response['data'] = serializer.data
            response['validations'] =[]
        else:
            response['status'] = status.HTTP_400_BAD_REQUEST
            response['data'] =[]
            response['message'] = 'Error en validaciones'
            response['validations'] = serializer.errors
    elif request.method == 'PUT':
        if id:
            folder = Folder.objects.get(id_folder=id)
            serializer = FolderSerializer(folder, data=request.data)
            if serializer.is_valid():
                serializer.save()
                response['status'] =status.HTTP_202_ACCEPTED
                response['message'] = 'Folder actualizado correctamente'
                response['validations'] = []
                response['data'] = serializer.data
            else:
                response['status'] =status.HTTP_400_BAD_REQUEST
                response['message'] = 'Error en validaciones'
                response['validations'] = serializer.errors
                response['data'] = []
        else:
            response['status'] =status.HTTP_400_BAD_REQUEST
            response['message'] = 'Id no enviado'
            response['validations'] = []
            response['data'] = []
    elif request.method == 'DELETE':
        if id:
            folder = Folder.objects.get(id_folder=id)
            folder.delete()
            response['status'] =status.HTTP_200_OK
            response['message'] = 'Eliminado correctamente'
            response['validations'] = []
            response['data'] =[]
        else:
            response['status'] =status.HTTP_400_BAD_REQUEST
            response['message'] = 'Id no enviado'
            response['validations'] = []
            response['data'] = []
    return Response(response)
@api_view(['GET','POST','DELETE','PUT'])
def taskApi(request,id=None):
    response = {}
    data = {}
    if id:
        try:
            task = Task.objects.get(id_task=id)
        except ObjectDoesNotExist:
            response['status'] = status.HTTP_404_NOT_FOUND
            response['message'] = 'No encontrado'
            response['data'] = []
            return Response(response)
    if request.method == 'GET':
        if id:
            task = Task.objects.get(id_task=id)
            serializer = TaskSerializer(task, many=False)
            response['status'] = status.HTTP_200_OK
            response['message'] = 'OK'
            response['data'] = serializer.data
        else:
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)
            response['status'] = status.HTTP_200_OK
            response['message'] = 'OK'
            response['data'] = serializer.data
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response['status'] = status.HTTP_201_CREATED
            response['message'] = 'Tarea creado correctamente'
            response['data'] = serializer.data
            response['validations'] =[]
        else:
            response['status'] = status.HTTP_400_BAD_REQUEST
            response['data'] =[]
            response['message'] = 'Error en validaciones'
            response['validations'] = serializer.errors
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
    return Response(response)
@api_view(['GET','POST','DELETE','PUT'])
def subtaskApi(request,id=None):
    response = {}
    data = {}
    if id:
        try:
            subtask = Sub_task.objects.get(id_sub_task=id)
        except ObjectDoesNotExist:
            response['status'] = status.HTTP_404_NOT_FOUND
            response['message'] = 'No encontrado'
            response['data'] = []
            return Response(response)
    if request.method == 'GET':
        if id:
            subtask = Sub_task.objects.get(id_sub_task=id)
            serializer = SubTaskSerializer(subtask, many=False)
            response['status'] = status.HTTP_200_OK
            response['message'] = 'OK'
            response['data'] = serializer.data
        else:
            subtasks = Sub_task.objects.all()
            serializer = SubTaskSerializer(subtasks, many=True)
            response['status'] = status.HTTP_200_OK
            response['message'] = 'OK'
            response['data'] = serializer.data
    elif request.method == 'POST':
        serializer = SubTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response['status'] = status.HTTP_201_CREATED
            response['message'] = 'Sub-tarea creada correctamente'
            response['data'] = serializer.data
            response['validations'] =[]
        else:
            response['status'] = status.HTTP_400_BAD_REQUEST
            response['data'] =[]
            response['message'] = 'Error en validaciones'
            response['validations'] = serializer.errors
    elif request.method == 'PUT':
        if id:
            subtask = Sub_task.objects.get(id_sub_task=id)
            serializer = SubTaskSerializer(subtask, data=request.data)
            if serializer.is_valid():
                serializer.save()
                response['status'] =status.HTTP_202_ACCEPTED
                response['message'] = 'Sub-tarea actualizada correctamente'
                response['validations'] = []
                response['data'] = serializer.data
            else:
                response['status'] =status.HTTP_400_BAD_REQUEST
                response['message'] = 'Error en validaciones'
                response['validations'] = serializer.errors
                response['data'] = []
        else:
            response['status'] =status.HTTP_400_BAD_REQUEST
            response['message'] = 'Id no enviado'
            response['validations'] = []
            response['data'] = []
    elif request.method == 'DELETE':
        if id:
            subtask = Sub_task.objects.get(id_sub_task=id)
            subtask.delete()
            response['status'] =status.HTTP_200_OK
            response['message'] = 'Eliminado correctamente'
            response['validations'] = []
            response['data'] =[]
        else:
            response['status'] =status.HTTP_400_BAD_REQUEST
            response['message'] = 'Id no enviado'
            response['validations'] = []
            response['data'] = []
    return Response(response)


