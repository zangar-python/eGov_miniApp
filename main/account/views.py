from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .account_class import Accounts_funtions
from rest_framework.permissions import AllowAny
from .main_info import main_info

class RegisterViews(APIView):
    permission_classes = [AllowAny]
    def post(self,request:Request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        if not username or not password or not email:
            return Response("Пустые поля")
        return Response(Accounts_funtions.register(username,password,email))

class LoginViews(APIView):
    permission_classes = [AllowAny]
    def post(self,request:Request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response("Пустые поля")
        return Response(Accounts_funtions.login(username,password,request))

class MainInfoViews(APIView):
    def get(self,request:Request):
        info = main_info(request)
        return Response(info.messages_info())