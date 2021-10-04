from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from user.models import Folder, Task, Sub_task, Project
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate

class SubTaskSerializer(serializers.ModelSerializer):
    task_name = serializers.ReadOnlyField(source='task.desc_task')
    class Meta:
        model = Sub_task
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    folder_name = serializers.ReadOnlyField(source='folder.name_folder')
    subtasks = SubTaskSerializer('subtasks',many=True, read_only=True)
    class Meta:
        model = Task
        fields =  ('id_task','img_task','desc_task','completed','folder','folder_name','created_at','updated_at', 'subtasks','title_task','due_date_task')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','name_project','user')
        read_only_fields = ('id',)


class UserSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(source='users',many=True, read_only=True)
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8)
    
    def create(self, validated_data):
       user = User(**validated_data) 
       user.set_password(validated_data['password'])
       user.save()
       return user

    class Meta:
        model = User
        fields = ('id','username','email','password','tasks','first_name','last_name')

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
