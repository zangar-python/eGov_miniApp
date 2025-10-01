from app1.serializers import Messages,MessageSerializer
from .serializers import UserSerializer

class main_info:
    def __init__(self,request):
        self.user = request.user
        pass
    
    def messages_info(self):
        messages:list[Messages] = self.user.messages.all().order_by("-created_at")
        res = {
            "user":UserSerializer(self.user).data,
            "messages":MessageSerializer(messages,many=True).data
        }
        return res