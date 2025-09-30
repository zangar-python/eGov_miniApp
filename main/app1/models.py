from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Messages(models.Model):
    title = models.TextField()
    user = models.ForeignKey(User,models.CASCADE,related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title[:15]}..."


class Queue(models.Model):
    title = models.CharField(max_length=50)
    users = models.ManyToManyField(User,related_name="queue")
    admins = models.ManyToManyField(User,related_name="admin_my_queue")
    
    def __str__(self):
        return self.title   