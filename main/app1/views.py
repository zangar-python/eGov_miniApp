from .to_queue import To_Queue
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class Queue_User_Views(APIView):
    def post(self,request:Request,id):
        user_func = To_Queue(request.user)
        return Response(user_func.login_to_queue(id))
    def get(self,request:Request,id):
        user_func = To_Queue(request.user)
        res = user_func.get_queue(id)
        return Response(res)
    def delete(self,request:Request,id):
        user_func = To_Queue(request.user)
        res = user_func.quit_the_queue(id)
        return Response(res)

class Queue_Admin_Get_User(APIView):
    def post(self,request:Request,id):
        user_obj = To_Queue(request.user)
        title = request.data.get("title")
        if not title:
            return Response({"err":"title пустая!!!"})
        res = user_obj.as_get_a_user(id,title)
        return Response(res)

class Queue_Views(APIView):
    def post(self,request:Request):
        user_func = To_Queue(request.user)
        title = request.data.get("title")
        if not title:
            return Response({"err":"title is null"})
        res = user_func.create_queue(title)
        return Response(res)

    