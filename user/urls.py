from django.urls import path
from user import views 

urlpatterns = [
    path('user/',views.userApi,name="userApi"),
    path('user',views.userApi,name="userApi"),
    path('user/<int:id>',views.userApi,name="userApi"),
    path('folder/',views.folderApi,name="folderApi"),
    path('folder',views.folderApi,name="folderApi"),
    path('folder/<int:id>',views.folderApi,name="folderApi"),
    path('task/',views.taskApi,name="taskApi"),
    path('task',views.taskApi,name="taskApi"),
    path('task/<int:id>',views.taskApi,name="taskApi"),
    path('subtask/',views.subtaskApi,name="subtaskApi"),
    path('subtask',views.subtaskApi,name="subtaskApi"),
    path('subtask/<int:id>',views.subtaskApi,name="subtaskApi"),
    path('login/',views.login,name="login"),
    path('login',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('register',views.register,name="register"),
]
