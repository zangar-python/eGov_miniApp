from django.urls import path
from .views import Queue_User_Views,Queue_Views,Queue_Admin_Get_User,admin_crud_views

urlpatterns = [
    path("",Queue_Views.as_view()),
    path("<int:id>/",Queue_User_Views.as_view()),
    path("<int:id>/get_user/",Queue_Admin_Get_User.as_view()),
    path("<int:id>/admin/",admin_crud_views.as_view())
]
