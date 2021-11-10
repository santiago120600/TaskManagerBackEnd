from django.shortcuts import render
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from django.contrib.auth.models import User  
from user.models import Folder, Task, Sub_task, Project, Task_file, Comment
from user.serializers import UserSerializer, FolderSerializer, TaskSerializer, SubTaskSerializer, LoginSerializer, ProjectSerializer, CommentSerializer, TaskFileSerializer, AddUserSerializer, AddUserToTaskSerializer, CreateProjectSerializer, AddUserToProjectSerializer

from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.permissions import IsAuthenticated, AllowAny

from django.db import transaction

@api_view(['GET','POST','DELETE','PUT'])
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
    try:
        project_id = request.GET['project_id']
    except:
        project_id = None
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
        elif project_id:
            try:
                task = Task.objects.filter(project_id=project_id)
                serializer = TaskSerializer(task, many=True)
                response['status'] = status.HTTP_200_OK
                response['message'] = 'OK'
                response['data'] = serializer.data
            except ObjectDoesNotExist:
                response['status'] = status.HTTP_404_NOT_FOUND
                response['message'] = 'No encontrado'
                response['data'] = []
                return Response(response)
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
            response['message'] = 'Tarea creada correctamente'
            response['data'] = serializer.data
            response['validations'] =[]
        else:
            response['status'] = status.HTTP_400_BAD_REQUEST
            response['data'] =[]
            response['message'] = 'Error en validaciones'
            response['validations'] = serializer.errors
    elif request.method == 'PUT':
        if id:
            task = Task.objects.get(id_task=id)
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                response['status'] =status.HTTP_202_ACCEPTED
                response['message'] = 'Tarea actualizada correctamente'
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
        task = Task.objects.get(id_task=id)
        task.delete()
    return Response(response)
@api_view(['GET','DELETE','PUT'])
def projectApi(request,id=None):
    response = {}
    try:
        user_id = request.GET['user_id']
    except:
        user_id = None
    if id:
        try:
            project = Project.objects.get(id=id)
        except ObjectDoesNotExist:
            response['status'] = status.HTTP_404_NOT_FOUND
            response['message'] = 'No encontrado'
            response['data'] = []
            return Response(response)
    if request.method == 'GET':
        if id:
            project = Project.objects.get(id=id)
            serializer = ProjectSerializer(project, many=False)
            response['status'] = status.HTTP_200_OK
            response['message'] = 'OK'
            response['data'] = serializer.data
        elif user_id:
            try:
                project = Project.objects.filter(users__id=user_id)
                print("PROJECT: ",project)
                serializer = ProjectSerializer(project, many=True)
                response['status'] = status.HTTP_200_OK
                response['message'] = 'OK'
                response['data'] = serializer.data
            except ObjectDoesNotExist:
                response['status'] = status.HTTP_404_NOT_FOUND
                response['message'] = 'No encontrado'
                response['data'] = []
                return Response(response)
        else:
            projects = Project.objects.all()
            serializer = ProjectSerializer(projects, many=True)
            response['status'] = status.HTTP_200_OK
            response['message'] = 'OK'
            response['data'] = serializer.data
    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response['status'] = status.HTTP_201_CREATED
            response['message'] = 'Proyecto creado correctamente'
            response['data'] = serializer.data
            response['validations'] =[]
        else:
            response['status'] = status.HTTP_400_BAD_REQUEST
            response['data'] =[]
            response['message'] = 'Error en validaciones'
            response['validations'] = serializer.errors
    elif request.method == 'PUT':
        if id:
            project = Project.objects.get(id=id)
            serializer = ProjectSerializer(project, data=request.data)
            if serializer.is_valid():
                serializer.save()
                response['status'] =status.HTTP_202_ACCEPTED
                response['message'] = 'Proyecto actualizado correctamente'
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
        project = Project.objects.get(id=id)
        project.delete()
    return Response(response)
@api_view(['GET','POST','DELETE','PUT'])
def subtaskApi(request,id=None):
    response = {}
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
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    response = {}
    data = {}
    serializer = LoginSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user, many=False)
        account = serializer.data
        response['status'] = status.HTTP_200_OK
        response['message'] = 'OK'
        data['id_user'] = account['id']
        # data['email'] = account['email']
        data['username'] = account['username']
        response['token'] = token.key
    else:
        response['status'] = status.HTTP_401_UNAUTHORIZED
        response['message'] = 'Credenciales incorrectas'
    response['data'] = data
    return Response(response)
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    response = {}
    data = {}
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        account = serializer.save()
        response['status'] =status.HTTP_201_CREATED
        response['message'] = 'Usuario creado'
        data['email'] = account.email
        data['username'] = account.username
        data['id_user'] = account.id
        response['token'] = Token.objects.get(user=account).key
        response['data'] = data
        response['validations'] = []
    else:
        response['status'] =status.HTTP_400_BAD_REQUEST
        response['data'] = []
        response['message'] = 'Error de validaciones'
        response['validations'] =serializer.errors 
    return Response(response)
@api_view(['GET','POST','DELETE','PUT'])
def commentApi(request,id=None):
    response = {}
    if id:
        try:
            comment = Comment.objects.get(id=id)
        except ObjectDoesNotExist:
            response['status'] = status.HTTP_404_NOT_FOUND
            response['message'] = 'No encontrado'
            response['data'] = []
            return Response(response)
    if request.method == 'GET':
        if id:
            comment = Comment.objects.get(id=id)
            serializer = CommentSerializer(comment, many=False)
            response['status'] = status.HTTP_200_OK
            response['message'] = 'OK'
            response['data'] = serializer.data
        else:
            comments = Comment.objects.all()
            serializer = CommentSerializer(comments, many=True)
            response['status'] = status.HTTP_200_OK
            response['message'] = 'OK'
            response['data'] = serializer.data
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response['status'] = status.HTTP_201_CREATED
            response['message'] = 'comentario creado correctamente'
            response['data'] = serializer.data
            response['validations'] =[]
        else:
            response['status'] = status.HTTP_400_BAD_REQUEST
            response['data'] =[]
            response['message'] = 'Error en validaciones'
            response['validations'] = serializer.errors
    elif request.method == 'PUT':
        if id:
            comment = Comment.objects.get(id=id)
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                response['status'] =status.HTTP_202_ACCEPTED
                response['message'] = 'comentario actualizado correctamente'
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
            comment = Comment.objects.get(id=id)
            comment.delete()
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
def taskFileApi(request,id=None):
    response = {}
    if id:
        try:
            file = Task_file.objects.get(id=id)
        except ObjectDoesNotExist:
            response['status'] = status.HTTP_404_NOT_FOUND
            response['message'] = 'No encontrado'
            response['data'] = []
            return Response(response)
    if request.method == 'GET':
        if id:
            file = Task_file.objects.get(id=id)
            serializer = TaskFileSerializer(file, many=False)
            response['status'] = status.HTTP_200_OK
            response['message'] = 'OK'
            response['data'] = serializer.data
        else:
            files = Task_file.objects.all()
            serializer = TaskFileSerializer(files, many=True)
            response['status'] = status.HTTP_200_OK
            response['message'] = 'OK'
            response['data'] = serializer.data
    elif request.method == 'POST':
        serializer = TaskFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response['status'] = status.HTTP_201_CREATED
            response['message'] = 'Archivo subido correctamente'
            response['data'] = serializer.data
            response['validations'] =[]
        else:
            response['status'] = status.HTTP_400_BAD_REQUEST
            response['data'] =[]
            response['message'] = 'Error en validaciones'
            response['validations'] = serializer.errors
    elif request.method == 'PUT':
        if id:
            file = Task_file.objects.get(id=id)
            serializer = TaskFileSerializer(file, data=request.data)
            if serializer.is_valid():
                serializer.save()
                response['status'] =status.HTTP_202_ACCEPTED
                response['message'] = 'Archivo actualizado correctamente'
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
            file = Task_file.objects.get(id=id)
            file.delete()
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
@api_view(['POST','DELETE'])
def userProject(request):
    response = {}
    validations = {}
    request_data = request.data
    serializer = AddUserSerializer(data=request.data)
    if serializer.is_valid():
        user_id = request_data['user']
        project_id = request_data['project']
        validations['user'] = ""
        validations['project'] = ""
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            validations['user'] = "Usuario no encontrado"
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            validations['project'] = "proyecto no encontrado"
        if validations['project'] != "" or validations['user'] != "":
            response['status'] = status.HTTP_404_NOT_FOUND
            response['message'] = 'No encontrado'
            response['validations'] = validations
            response['data'] = []
            return Response(response)
        if request.method == 'POST':
            project.users.add(user)
            response['status'] =status.HTTP_200_OK
            response['message'] = 'Usuario agregado al proyecto'
            response['data'] = serializer.data
            response['validations'] = []
        if request.method == 'DELETE':
            project.users.remove(user)
            response['status'] =status.HTTP_200_OK
            response['message'] = 'Eliminado correctamente'
            response['validations'] = []
            response['data'] =[]
    else:    
        response['status'] = status.HTTP_400_BAD_REQUEST
        response['data'] =[]
        response['message'] = 'Error en validaciones'
        response['validations'] = serializer.errors
    return Response(response)
@api_view(['POST','DELETE'])
def userTask(request):
    response = {}
    validations = {}
    request_data = request.data
    serializer = AddUserToTaskSerializer(data=request.data)
    if serializer.is_valid():
        user_id = request_data['user']
        task_id = request_data['task']
        validations['user'] = ""
        validations['task'] = ""
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            validations['user'] = "Usuario no encontrado"
        try:
            task = Task.objects.get(id_task=task_id)
        except Task.DoesNotExist:
            validations['task'] = "Tarea no encontrada"
        if validations['task'] != "" or validations['user'] != "":
            response['status'] = status.HTTP_404_NOT_FOUND
            response['message'] = 'No encontrado'
            response['validations'] = validations
            response['data'] = []
            return Response(response)
        if request.method == 'POST':
            task.assigned_users.add(user)
            response['status'] =status.HTTP_200_OK
            response['message'] = 'Usuario agregado a la tarea'
            response['data'] = serializer.data
            response['validations'] = []
        if request.method == 'DELETE':
            task.assigned_users.remove(user)
            response['status'] =status.HTTP_200_OK
            response['message'] = 'Eliminado correctamente'
            response['validations'] = []
            response['data'] =[]
    else:    
        response['status'] = status.HTTP_400_BAD_REQUEST
        response['data'] =[]
        response['message'] = 'Error en validaciones'
        response['validations'] = serializer.errors
    return Response(response)
@api_view(['POST'])
@transaction.atomic
def createProject(request):
    response = {}
    serializer = CreateProjectSerializer(data=request.data)
    if serializer.is_valid():
        # crear proyecto
        project = Project.objects.create(name_project=request.data['name_project'])
        #checar que la persona existe
        try:
            user = User.objects.get(id=request.data['user'])
        except User.DoesNotExist:
            response['status'] = status.HTTP_404_NOT_FOUND
            response['message'] = 'No encontrado'
            response['validations'] = [{'user':'No encontrado'}]
            response['data'] = []
            return Response(response)
        #agregar a la persona
        project.users.add(user)
        response['status'] = status.HTTP_201_CREATED
        response['message'] = 'Proyecto creado correctamente'
        response['data'] = serializer.data
        response['validations'] =[]
    else:
        response['status'] = status.HTTP_400_BAD_REQUEST
        response['data'] =[]
        response['message'] = 'Error en validaciones'
        response['validations'] = serializer.errors
    return Response(response)
@api_view(['GET'])
def searchUser(request):
    response = {}
    data = {}
    try:
        request.data['user_email']
    except:
        response['status'] = status.HTTP_400_BAD_REQUEST
        response['message'] = ' Error en validaciones'
        response['validations'] = [{'user_email':'El campo es requerido'}]
        response['data'] = []
        return Response(response)
    try:
        user = User.objects.get(email=request.data['user_email'])
    except User.DoesNotExist:
        response['status'] = status.HTTP_404_NOT_FOUND
        response['message'] = 'No encontrado'
        response['validations'] = [{'user':'No encontrado'}]
        response['data'] = []
        return Response(response)
    user = User.objects.get(email__exact=request.data['user_email'])
    response['status'] = status.HTTP_200_OK
    response['message'] = 'OK'
    data['email'] = user.email
    data['username'] = user.username
    data['id'] = user.id
    response['data'] = data
    return Response(response)
@api_view(['POST'])
def addUserProject(request):
    response = {}
    serializer = AddUserToProjectSerializer(data=request.data)
    if serializer.is_valid():
        # buscar el username si existe entonces agregarlo al proyecto
        try:
            user = User.objects.get(username=request.data['username'])
        except User.DoesNotExist:
            #si no existe el usario mandar un no encontrado
            response['status'] = status.HTTP_404_NOT_FOUND
            response['message'] = 'No encontrado'
            response['validations'] = [{'username':'No encontrado'}]
            response['data'] = []
            return Response(response)
        # checar si existe el proyecto
        try:
            project = Project.objects.get(id=request.data['project'])
        except Project.DoesNotExist:
            response['status'] = status.HTTP_404_NOT_FOUND
            response['message'] = 'No encontrado'
            response['validations'] = [{'project':'No encontrado'}]
            response['data'] = []
            return Response(response)
        project.users.add(user)
        response['status'] = status.HTTP_201_CREATED
        response['message'] = 'Usuario agregado correctamente'
        response['data'] = serializer.data
        response['validations'] =[]
    else:    
        response['status'] = status.HTTP_400_BAD_REQUEST
        response['data'] =[]
        response['message'] = 'Error en validaciones'
        response['validations'] = serializer.errors
    return Response(response)
