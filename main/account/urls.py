from django.urls import path
from .views import RegisterViews,LoginViews

urlpatterns = [
    path("login/",LoginViews.as_view()),
    path("register/",RegisterViews.as_view())
]
