from django.urls import path
from user import views 

urlpatterns = [
    path('user/',views.userApi,name="userApi"),
    path('user/<int:id>',views.userApi,name="userApi"),
]
