from rest_framework import serializers
from user.models import User, Folder, Task, Sub_task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_task
        fields = '__all__'