from rest_framework.request import Request
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from rest_framework.authentication import authenticate

class Accounts_funtions:
    def __init__(self,user):
        self:User = user
        pass
    @staticmethod
    def register(username,password,email):
        if User.objects.filter(username=username).exists():
            return "Пользователь с таким именем уже существует"
        if len(password) < 8:
            return "Пароль не надежен"
        if not Accounts_funtions.email_exists_code(email):
            return "Емайл не потдверждается"
        user = User.objects.create_user(username,email,password)
        token,_ = Token.objects.get_or_create(user=user)
        return {
            "created":True,
            "user":UserSerializer(user).data,
            "token":token.key
        }
    @staticmethod
    def login(username,password,request):
        user = authenticate(request=request,username=username,password=password)
        if not user:
            return "Такого пользователья не существует"
        token,_ = Token.objects.get_or_create(user=user)
        return {
            "logined":True,
            "user":UserSerializer(user).data,
            "token":token.key
        }
    
    @staticmethod 
    def email_exists_code(email):
        return True