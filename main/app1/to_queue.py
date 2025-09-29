from .models import Queue,QueueUsers
from django.shortcuts import get_object_or_404


class To_Queue:
    def __init__(self,user):
        self.user = user
        pass
    
    def if_user_admin(self,queue):
        # queue = get_object_or_404(Queue,id=id)
        if queue.admins.filter(id=self.user.id).exists():
            return True
        return False
    def if_user_in_queue(self,queue):
        # queue = get_object_or_404(Queue,id=id)
        if queue.users.filter(id=self.user.id).exists():
            return True
        return False
    
    def login_to_queue(self,id):
        queue = get_object_or_404(Queue,id=id)
        _admin = self.if_user_admin(queue)
        _user = self.if_user_in_queue(queue)
        if _admin or _user:
            return False
        queue.users.add(self.user)
        return True
    
        
        