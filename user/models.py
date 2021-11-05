from django.db import models
from django.contrib.auth.models import User  
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Project(models.Model):
    name_project = models.CharField(max_length=80)
    img_task = models.ImageField(upload_to='uploads/',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

# tabla para relacionar los proyectos con las personas
class User_Project(models.Model):
    user  = models.ForeignKey(User, null=False,on_delete=models.CASCADE)
    project = models.ForeignKey(Project, null=False, on_delete=models.CASCADE)
    user_type = (
        ('admin','admin'),
        ('regular','regular')
    )
    type_user = models.CharField(max_length=10, choices=user_type, default=user_type[1])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

class Folder(models.Model):
    id_folder  = models.AutoField(primary_key=True)
    name_folder = models.CharField(max_length=80)
    desc_folder = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name_folder

class Task(models.Model):
    id_task  = models.AutoField(primary_key=True)
    img_task = models.ImageField(upload_to='uploads/',blank=True, null=True)
    title_task = models.CharField(max_length=80,null=True,blank=True)
    due_date_task = models.DateField(null=True,blank=True)
    desc_task = models.TextField()
    completed = models.BooleanField(default=False)
    folder = models.ForeignKey(Folder, related_name="tasks", null=True,blank=True,on_delete=models.CASCADE)
    project = models.ForeignKey(Project, null=False, blank="False",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.desc_task

# tabla para relacionar los archivos con una tarea
class Task_file(models.Model):
    task = models.ForeignKey(Task, null=False,on_delete=models.CASCADE)
    file = models.FileField(blank=False, null=False, upload_to='uploads/')

# tabla para asignar las tareas a cierta o ciertas personas
class Task_User(models.Model):
    task = models.ForeignKey(Task, null=False,on_delete=models.CASCADE)
    user  = models.ForeignKey(User, null=False,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

class Comment(models.Model):
    desc_comment = models.TextField()
    task = models.ForeignKey(Task, null=False,on_delete=models.CASCADE)
    user  = models.ForeignKey(User, null=False,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

class Sub_task(models.Model):
    id_sub_task = models.AutoField(primary_key=True)
    desc_sub_task = models.TextField()
    completed = models.BooleanField(default=False)
    task = models.ForeignKey(Task, null=False,on_delete=models.CASCADE, related_name="subtasks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.desc_sub_task

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
