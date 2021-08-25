from django.contrib import admin
from .models import User, Folder, Task, Sub_task

# Register your models here.
@admin.register(Folder, Task, Sub_task)
class UserAdmin(admin.ModelAdmin):
    pass

