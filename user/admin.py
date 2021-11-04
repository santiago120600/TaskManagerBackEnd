from django.contrib import admin
from .models import User, Folder, Task, Sub_task, Project, User_Project, Task_file, Task_User, Comment

# Register your models here.
@admin.register(Folder, Task, Sub_task, Project, User_Project, Task_file, Task_User, Comment)
class UserAdmin(admin.ModelAdmin):
    pass

