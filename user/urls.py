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
    path('project',views.projectApi,name="projectApi"),
    path('project/',views.projectApi,name="projectApi"),
    path('project/<int:id>',views.projectApi,name="projectApi"),
    path('subtask/',views.subtaskApi,name="subtaskApi"),
    path('subtask',views.subtaskApi,name="subtaskApi"),
    path('subtask/<int:id>',views.subtaskApi,name="subtaskApi"),
    path('login/',views.login,name="login"),
    path('login',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('register',views.register,name="register"),
    path('comment/',views.commentApi,name="commentApi"),
    path('comment',views.commentApi,name="commentApi"),
    path('comment/<int:id>',views.commentApi,name="commentApi"),
    path('file/',views.taskFileApi,name="taskFileApi"),
    path('file',views.taskFileApi,name="taskFileApi"),
    path('file/<int:id>',views.taskFileApi,name="taskFileApi"),
    path('userproject',views.userProject,name="userproject"),
    path('userproject/',views.userProject,name="userProject"),
    path('usertask/',views.userTask,name="userTask"),
    path('usertask',views.userTask,name="userTask"),
    path('createproject',views.createProject,name="createProject"),
    path('createproject/',views.createProject,name="createProject"),
    path('searchuser/',views.searchUser,name="searchUser"),
    path('searchuser',views.searchUser,name="searchUser"),
    path('adduserproject',views.addUserProject,name="addUserProject"),
    path('adduserproject/',views.addUserProject,name="addUserProject"),
]
