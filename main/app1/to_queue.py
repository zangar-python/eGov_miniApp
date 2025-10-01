from .models import Queue,Messages
from django.shortcuts import get_object_or_404
from account.serializers import UserSerializer
import redis

from django.contrib.auth.models import User
from .serializers import QueueSerializer

from .tasks import send_message_to_user

r = redis.Redis("localhost",6379,0)

class To_Queue:
    def __init__(self,user):
        self.user = user
        pass
    
    def create_queue(self,title):
        queue = Queue.objects.create(
            title=title,
        )
        queue.admins.add(self.user)
        return self.RESULT({
            "result":f"Успешно создано! ID:{queue.id}",
            "queue":QueueSerializer(queue).data 
        }
        )
    
    # ADMINS
    
    def if_user_admin(self,queue):
        # queue = get_object_or_404(Queue,id=id)
        if queue.admins.filter(id=self.user.id).exists():
            return True
        return False
    
    def add_admin(self,user_id,queue_id):
        queue = get_object_or_404(Queue,id=queue_id)
        _admin = self.if_user_admin(queue)
        if not _admin:
           return self.RESULT("Вы не можете добавлять админов") 
        _isin_admin = queue.admins.filter(id=user_id).exists()
        if _isin_admin:
            return self.RESULT("Этот пользователь уже в списке админов")
        queue.admins.add(user_id)
        return self.RESULT(
            "Пользователь успешно добавлен в админ"
        )
    
    def delete_admin(self,user_id,queue_id):
        queue = get_object_or_404(Queue,id=queue_id)
        _admin = self.if_user_admin(queue)
        if not _admin:
            return self.RESULT("Вы не можете удалять админов")
        _isin_admin = queue.admins.filter(id=user_id).exclude(id=self.user.id).exists()
        if not _isin_admin:
            return "Этот пользователь не админ или вы пытаетесь удалить самого себя"
        queue.admins.remove(user_id)
        return self.RESULT("Успешно удален из списка админов")
        
    # MIDDLEWERS
    
    
    def if_user_in_queue(self,queue):
        # queue = get_object_or_404(Queue,id=id)
        if queue.users.filter(id=self.user.id).exists():
            return True
        return False
    
    # РЕЗУЛЬТАТ ВСЕГДА ДОЛЖЕН ИДТИ ВОТ ЗДЕСЬ
    
    def RESULT(self,data):
        result = {
            "user":UserSerializer(self.user).data,
            "connect_":True,
            "data":data
        }
        return result
    
    
    
    
    # METHODS
    
    def login_to_queue(self,id):
        queue = get_object_or_404(Queue,id=id)
        _admin = self.if_user_admin(queue)
        _user = self.if_user_in_queue(queue)
        if _admin or _user:
            return self.RESULT({
                "data":"Вы уже находитесь в очереди",
                "queue":queue.title
            })
        queue.users.add(self.user)
        r.lpush(f"queue:{id}",self.user.id)
        return self.RESULT("Вы в очереди")
    
    def quit_the_queue(self,id):
        queue = get_object_or_404(Queue,id=id)
        is_user = self.if_user_in_queue(queue)
        if not is_user:
            return self.RESULT({
                "data":"Вы не зарегестрировались к этому списку"
            })
        r.lrem(f"queue:{id}",0,self.user.id)
        queue.users.remove(self.user.id)
        return self.RESULT({
            "data":"Вы вышли со списка",
            "queue_id":queue.id
        })
    
    def get_queue(self,id):
        queue = get_object_or_404(Queue,id=id)
        queue_data = [ i.decode() for i in r.lrange(f"queue:{id}",0,-1)]
        queue_data.reverse()
        return self.RESULT({
            "queue":QueueSerializer(queue).data,
            "users_list":queue_data
        })
        
    def as_get_a_user(self,id,title):
        queue = get_object_or_404(Queue,id=id)
        _admin = self.if_user_admin(queue)
        if not _admin:
            return self.RESULT({
                "data":"Вы не являетесь админом",
                "queue_id":queue.id
            })
        user_id =  r.rpop(f"queue:{id}").decode()
        user = get_object_or_404(User,id=user_id)
        queue.users.remove(user)
        send_message_to_user.delay(user_id,title)
        return self.RESULT({
            "user_in_queque":UserSerializer(user).data,
            "Message_sended":True
        })
        