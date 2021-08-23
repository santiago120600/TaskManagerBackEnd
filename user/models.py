from django.db import models

# Create your models here.
class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=80)
    user_password = models.CharField(max_length=80)
    name_user = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_email

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
    img_task = models.ImageField(upload_to='uploads')
    desc_task = models.TextField()
    completed = models.BooleanField(default=False)
    user  = models.ForeignKey(User, null=False,on_delete=models.CASCADE, related_name="users")
    folder = models.ForeignKey(Folder, related_name="tasks", null=False,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.desc_task

class Sub_task(models.Model):
    id_sub_task = models.AutoField(primary_key=True)
    desc_sub_task = models.TextField()
    completed = models.BooleanField(default=False)
    task = models.ForeignKey(Task, null=False,on_delete=models.CASCADE, related_name="subtasks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.desc_sub_task


