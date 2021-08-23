from rest_framework import serializers
from user.models import User, Folder, Task, Sub_task

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
    class Meta:
        model = User
        fields = '__all__'

class FolderSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer('tasks',many=True, read_only=True)
    class Meta:
        model = Folder
        fields = '__all__'
