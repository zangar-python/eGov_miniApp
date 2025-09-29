from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .account_class import Accounts_funtions

class RegisterViews(APIView):
    def post(self,request:Request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        if not username or not password or not email:
            return Response("Пустые поля")
        return Response(Accounts_funtions.register(username,password,email))

class LoginViews(APIView):
    def post(self,request:Request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response("Пустые поля")
        return Response(Accounts_funtions.login(username,password,request))

