from celery import shared_task
from .models import Messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

@shared_task
def send_message_to_user(user_id,title):
    user = get_object_or_404(User,id=user_id)
    title_ = f"Очередь дошло к вам: {title}"
    Messages.objects.create(
        user = user,
        title = title_
    )
    return True