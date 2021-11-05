from django.contrib import admin
from .models import User, Folder, Task, Sub_task, Project, Task_file, Comment

# Register your models here.
@admin.register(Folder, Task, Sub_task, Project, Task_file, Comment)
class UserAdmin(admin.ModelAdmin):
    pass

