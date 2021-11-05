from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from user.models import Folder, Task, Sub_task, Project, User_Project, Task_file, Task_User, Comment
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
        fields =  ('id_task','img_task','desc_task','completed','folder','folder_name','created_at','updated_at', 'subtasks','title_task','due_date_task', 'project')

class TaskFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_file
        fields = ('desc_task','project')

class TaskUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_User
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8)
    
    def create(self, validated_data):
       user = User(**validated_data) 
       user.set_password(validated_data['password'])
       user.save()
       return user

    class Meta:
        model = User
        fields = ('id','username','email','password','first_name','last_name')

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer('user_set',many=False, read_only=True)
    task =  TaskSerializer('task_set',many=False, read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'

class UserProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Project
        fields = ('user','project')

class ProjectSerializer(serializers.ModelSerializer):
    projects = UserProjectSerializer('project_set',many=True, read_only=True)
    print(projects)
    class Meta:
        model = Project
        fields = ('id','name_project','projects')
        read_only_fields = ('id',)
        #tengo una tabla intermedia User_Project fields user y project
        #debo traer todos los usuarios que tengan el id de ese proyecto

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
