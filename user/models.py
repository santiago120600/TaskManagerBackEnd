from django.db import models

# Create your models here.
class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=80)
    user_password = models.CharField(max_length=80)
    name_user = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)

class Folder(models.Model):
    id_folder  = models.AutoField(primary_key=True)
    name_folder = models.CharField(max_length=80)
    desc_folder = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

class Task(models.Model):
    id_task  = models.AutoField(primary_key=True)
    img_task = models.CharField(max_length=150)
    desc_task = models.TextField()
    completed = models.BooleanField(default=False)
    user  = models.ForeignKey(User, null=False,on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, null=False,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

class Sub_task(models.Model):
    id_sub_task = models.AutoField(primary_key=True)
    desc_sub_task = models.TextField()
    completed = models.BooleanField(default=False)
    task = models.ForeignKey(Task, null=False,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)


