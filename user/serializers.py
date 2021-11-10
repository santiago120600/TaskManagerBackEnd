from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from user.models import Folder, Task, Sub_task, Project, Task_file, Comment
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate

class SubTaskSerializer(serializers.ModelSerializer):
    task_name = serializers.ReadOnlyField(source='task.desc_task')
    class Meta:
        model = Sub_task
        fields = "__all__"

class TaskFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_file
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())], write_only=True)
    password = serializers.CharField(min_length=8, write_only=True)
    
    def create(self, validated_data):
       user = User(**validated_data) 
       user.set_password(validated_data['password'])
       user.save()
       return user

    class Meta:
        model = User
        fields = ('id','username','email','password','first_name','last_name')

class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    files = TaskFileSerializer(many=True, read_only=True)
    comments = CommentSerializer('tasks_set', many=True, read_only=True)  # No me regresa nada
    folder_name = serializers.ReadOnlyField(source='folder.name_folder')
    subtasks = SubTaskSerializer('subtasks',many=True, read_only=True)
    assigned_users = UserSerializer('assigned_users_set', many=True, required=False)
    class Meta:
        model = Task
        fields =  ('id_task','img_task','desc_task','completed','folder','folder_name','created_at','updated_at', 'subtasks','title_task','due_date_task', 'project', 'assigned_users', 'files', 'comments')
        optional_fields = ['assigned_users', ]
        # depth = 1

class ProjectSerializer(serializers.ModelSerializer):
    users =  UserSerializer('users_set',many=True, required=False)
    class Meta:
        model = Project
        fields = ('name_project','id', 'users')
        optional_fields = ['users', ]

class CreateProjectSerializer(serializers.Serializer):
    name_project = serializers.CharField(max_length=80)
    user = serializers.IntegerField()

class AddUserSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    project = serializers.IntegerField()


class AddUserToTaskSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    task = serializers.IntegerField()

class AddUserToProjectSerializer(serializers.Serializer):
    project = serializers.IntegerField()
    username = serializers.CharField(max_length=80)


class FolderSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer('tasks',many=True, read_only=True)
    class Meta:
        model = Folder
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(
        label=("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=128,
        write_only=True
    )

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request=self.context.get('request'), username=username, password=password)
        if not user:
            msg = ('Las credenciales son incorrectas')
            raise serializers.ValidationError(msg, code='authorization')

        data['user'] = user
        return data
