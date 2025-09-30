from django.urls import path
from .views import Queue_User_Views,Queue_Views,Queue_Admin_Get_User

urlpatterns = [
    path("",Queue_Views.as_view()),
    path("<int:id>/",Queue_User_Views.as_view()),
    path("<int:id>/get_user/",Queue_Admin_Get_User.as_view())
]
