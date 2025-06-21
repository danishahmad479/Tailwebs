from django.urls import path 
from .views import *
urlpatterns = [
 
    path("",index,name="index"),
    path("register/",register,name="register"),
    path("login/",user_login,name="login"),
    path('logout/',user_logout,name="logout"),
    path('add_record/',add_record,name='add_record'),
    path('edit/<int:record_id>/',edit_record, name='edit_record'),
    path('delete/<int:record_id>/', delete_record, name='delete_record'),
]
