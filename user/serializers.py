from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from user.models import Folder, Task, Sub_task
from django.contrib.auth.models import User  
# from django.contrib.auth.hashers import make_password #Encriptar contraseña

class SubTaskSerializer(serializers.ModelSerializer):
    task_name = serializers.ReadOnlyField(source='task.desc_task')
    class Meta:
        model = Sub_task
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.name_user')
    folder_name = serializers.ReadOnlyField(source='folder.name_folder')
    subtasks = SubTaskSerializer('subtasks',many=True, read_only=True)
    class Meta:
        model = Task
        fields =  ('id_task','img_task','desc_task','completed','user','user_name','folder','folder_name','created_at','updated_at', 'subtasks')

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
        fields = ('id','username','email','password','tasks')

class FolderSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer('tasks',many=True, read_only=True)
    class Meta:
        model = Folder
        fields = '__all__'
