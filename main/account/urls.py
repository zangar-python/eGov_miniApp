from django.urls import path
from .views import RegisterViews,LoginViews,MainInfoViews

urlpatterns = [
    path("login/",LoginViews.as_view()),
    path("register/",RegisterViews.as_view()),
    path("",MainInfoViews.as_view())
]

